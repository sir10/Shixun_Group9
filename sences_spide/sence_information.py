from selenium import webdriver
from lxml import etree
import json
import time
import re

city_name_list = ['shanghai', 'suzhou', 'xiamen', 'xian',
                  'zhangjiajie']

city_dict = json.load(open('city_dict.json', 'r', encoding='utf-8'))

url_list = ['https://you.ctrip.com/sight/{}.html'.format(item + city_dict[item]) for item in city_name_list]

class tourist_routes(object):
    def __init__(self,city_url):
        self.page = 1
        self.url = city_url
        self.option = webdriver.ChromeOptions()
        self.city = re.sub('\d+', '', city_url.split('/')[-1].split('.')[0])
        '''
            self.option.add_argument('--headless')
            self.option.add_argument('--no-sandbox')
            self.option.add_argument('--disable-dev-shm-usage')
            self.option.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(options=self.option, executable_path='/usr/local/bin/chromedriver')
        '''
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)
    def get_data(self):
        """
        进入页面
        :return:本页页面data
        """

        # 模拟页面滚动,确保数据加载完毕
        self.driver.execute_script('var q=document.documentElement.scrollTop=10000')
        # 获得网页数据
        data = self.driver.page_source

        return data

    def parse_data(self, data):
        """
        解析，提取数据
        :param data: 本页网页data
        :return: 本页数据
        """

        data_list = []
        # 获取、解析
        try:
            node_list = self.driver.find_elements_by_class_name('list_mod2')
            for node in node_list:
                temp = {}
                try:
                    detail_url = node.find_element_by_xpath('div[2]/dl/dt/a').get_attribute('href')
                    temp['url'] = detail_url
                    temp['name'] = node.find_element_by_xpath('div[2]/dl/dt/a').text
                except:
                    continue
                # driver1.quit()
                # 获取、解析
                opt = webdriver.ChromeOptions()
                opt.add_argument('--headless')
                '''
                    opt.add_argument('--no-sandbox')
                    opt.add_argument('--disable-dev-shm-usage')
                    opt.add_argument('--disable-gpu')
                    driver1 = webdriver.Chrome(options=opt, executable_path='/usr/local/bin/chromedriver')
                '''
                driver1 = webdriver.Chrome(options=opt)
                driver1.implicitly_wait(5)
                driver1.get(detail_url)
                # 等待3秒，等待网页相应
                # 模拟页面滚动
                driver1.execute_script('var q=document.documentElement.scrollTop=10000')

                # 获取、解析详情页
                detail_page = driver1.page_source
                hr = etree.HTML(detail_page)

                temp['url'] = detail_url
                try:
                    temp['name'] = hr.xpath('//*[@id="__next"]/div[3]/div/div[3]/div[2]/div[1]/h1/text()')[0]
                except:
                    temp['name'] = ''
                try:
                    temp['rank'] = int(driver1.find_element_by_xpath('//*[@id="__next"]/div[3]/div/div[3]/div[2]/div[1]/div/span').text[0])
                except:
                    temp['rank'] = -1

                try:
                    picture_urls = driver1.find_elements_by_xpath('//*[@id="__next"]/div[3]/div/div[3]/div[1]/div[2]/div/div')
                    p = re.compile(r'["](.*?)["]', re.S)  # 最小匹配
                    temp['pic_url'] = []
                    for picture_url in picture_urls:
                        p_url = re.findall(p, picture_url.get_attribute('style'))[0]
                        temp['pic_url'].append(p_url)
                except:
                    temp['pic_url'] = ''

                try:
                    temp['address'] = driver1.find_elements_by_class_name('baseInfoText')[0].text
                except:
                    temp['address'] = ''

                try:
                    tele = hr.xpath('//*[@id="__next"]/div[3]/div/div[3]/div[2]/div[4]/div[3]/p[1]/text()')
                    if '官方电话' in tele:
                        temp['tel'] = driver1.find_element_by_xpath(
                            '//*[@id="__next"]/div[3]/div/div[3]/div[2]/div[4]/div[3]/p[2]').text
                except:
                    temp['tel'] = ''

                # temp['sence_details'] = {}
                detail = {}

                try:
                    intro_t = hr.xpath('//*[@id="__next"]/div[3]/div/div[4]/div[1]/div[2]/div/div/text()')
                    if '景点介绍' in intro_t:
                        Introductions = driver1.find_elements_by_xpath(
                            '//*[@id="__next"]/div[3]/div/div[4]/div[1]/div[2]/div/div[2]/div/div/p')
                        d_introduction = []
                        for introduction in Introductions:
                            introduction = introduction.text
                            if introduction != '':
                                d_introduction.append(introduction)
                        detail['sence_introduction'] = d_introduction
                except:
                    pass

                try:
                    if '开放时间' in intro_t:
                        detail['time'] = driver1.find_element_by_xpath(
                            '//*[@id="__next"]/div[3]/div/div[4]/div[1]/div[2]/div/div[4]').text
                        # print(detail['开放时间'])
                except:
                    pass

                try:
                    if '优待政策' in intro_t:  # //*[@id="__next"]/div[3]/div/div[4]/div[1]/div[2]/div/div[3]
                        policys = driver1.find_elements_by_xpath(
                            '//*[@id="__next"]/div[3]/div/div[4]/div[1]/div[2]/div/div[6]/div')
                        d_policy = []
                        for policy in policys:
                            policy = policy.text
                            d_policy.append(policy)
                        detail['policy'] = d_policy
                except:
                    pass

                try:
                    if '服务设施' in intro_t:
                        servers = driver1.find_elements_by_xpath(
                            '//*[@id="__next"]/div[3]/div/div[4]/div[1]/div[2]/div/div[8]/div')
                        d_server = []
                        for server in servers:
                            server = server.text
                            d_server.append(server)
                        detail['service'] = d_server
                except:
                    pass

                try:
                    if '交通攻略' in intro_t:
                        detail['traffic'] = hr.xpath('//*[@id="__next"]/div[3]/div/div[4]/div[1]/div[2]/div/div[10]/text()')
                except:
                    pass

                try:
                    if '必看贴士' in intro_t:
                            tips = driver1.find_elements_by_xpath(
                                '//*[@id="__next"]/div[3]/div/div[4]/div[1]/div[2]/div/div[12]/div/p[1]/text()')
                            d_tip = []
                            for tip in tips:
                                tip = tip.text
                                d_tip.append(tip)
                            detail['tip'] = d_tip
                except:
                    pass
                temp['sence_details'] = detail

                try:
                    temp['score'] = float(hr.xpath('//*[@id="commentModule"]/div[2]/span/text()')[0])
                except:
                    temp['score'] = -1

                try:
                    key_words = driver1.find_elements_by_class_name('hotTag')
                    temp['key_word'] = []
                    for key_word in key_words:
                        # 筛去无意义的关键词
                        key_word = key_word.text.split('(')[0]
                        if '最新' in key_word:
                            continue
                        elif '好评' in key_word:
                            continue
                        elif '中评' in key_word:
                            continue
                        elif '差评' in key_word:
                            continue
                        elif '有图' in key_word:
                            continue
                        elif '追评' in key_word:
                            continue
                        elif '全部' in key_word:
                            continue
                        elif '来自' in key_word:
                            continue
                        elif '带图' in key_word:
                            continue
                        elif '视频' in key_word:
                            continue
                    else:
                        temp['key_word'].append(key_word)
                except:
                    pass
                try:
                    users = hr.xpath(
                        '/html/body/div[2]/div[3]/div/div[4]/div[1]/div[4]/div/div[5]/div/div[1]/div[2]/text()')

                    marks = hr.xpath(
                        '/html/body/div[2]/div[3]/div/div[4]/div[1]/div[4]/div/div[5]/div/div[2]/div[1]/span/text()[1]')

                    #获取每个用户的评论信息
                    comments = hr.xpath(
                        '/html/body/div[2]/div[3]/div/div[4]/div[1]/div[4]/div/div[5]/div/div[2]/div[2]/text()')

                    # 构建需要的格式
                    comment = []
                    for i in range(0, len(comments)):
                        com = {'user_name': users[i], 'user_score': float(marks[i]), 'user_comment': str(comments[i]).split("\n")[0]}
                        comment.append(com)
                    temp['comments'] = comment
                except:
                    pass
                print(temp)
                data_list.append(temp)
                driver1.quit()
        except:
            pass
        return data_list

    def save_data(self, data_list):
        """
        保存数据，一页保存一次
        :param data_list: 刚刚爬取的页面数据
        :return: None
        """
        for i in data_list:
            data = json.dumps(i, indent=4, ensure_ascii=False)
            with open(self.city + '.json', 'a', encoding='utf-8') as f:
                data = str(data) + ',\n'
                f.write(data)
                f.close()
        print('-------------第 ' + str(self.page) + ' 页已写入文件-------------')

    def next_page(self):
        #翻页操作
        try:
            final_page = self.driver.find_element_by_class_name('nextpage').get_attribute('class')
            if 'disabled' in final_page:
                return -1
            else:
                # self.driver.find_element_by_class_name('nextpage').click()
                next_page_url = self.driver.find_element_by_class_name('nextpage').get_attribute('href')
                self.driver.get(next_page_url)
                self.page = self.page + 1
                return self.page
        except:
            pass
        #class="pagination_div_icon pagination_div_icon_right pagination_div_icon_disabled"

    def run(self):
        """
        总控函数
        :return: None
        """

        while True:
            data = self.get_data()
            data_list = self.parse_data(data)
            if data_list is None:
                print('空值')
                break
            self.save_data(data_list)
            # id = self.next_page()
            time.sleep(1)
            if id == -1:
                break
        self.driver.quit()


if __name__ == '__main__':
    for city_url in url_list:
        spider_routes = tourist_routes(city_url)
        spider_routes.run()
