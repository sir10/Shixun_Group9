from selenium import webdriver
from lxml import etree
import json
import time
import re

city_name_list = ['kunming', 'lijiang', 'nanjing',
                  'qingdao', 'sanya', 'shanghai', 'suzhou', 'xiamen', 'xian', 'zhangjiajie']

city_dict = json.load(open('city_dict.json', 'r', encoding='utf-8'))

url_list = ['https://you.ctrip.com/sight/{}.html'.format(item + city_dict[item]) for item in city_name_list]

class tourist_routes(object):
    def __init__(self, city_url):
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
        self.driver.implicitly_wait(5)
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
        node_list = self.driver.find_elements_by_class_name('list_mod2')
        for node in node_list:
            temp = {}
            detail_url = node.find_element_by_xpath('div[2]/dl/dt/a').get_attribute('href')
            temp['url'] = detail_url
            temp['name'] = node.find_element_by_xpath('div[2]/dl/dt/a').text
            print(temp)
            data_list.append(temp)
        return data_list

    def save_data(self, data_list):
        for i in data_list:
            data = json.dumps(i, indent=4, ensure_ascii=False)
            with open('./ticket_url/' + self.city + '.json', 'a', encoding='utf-8') as f:
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
            id = self.next_page()
            time.sleep(1)
            if id == -1:
                break
        self.driver.quit()


if __name__ == '__main__':
    for url_item in url_list:
        spider_routes = tourist_routes(url_item)
        spider_routes.run()
