from selenium import webdriver
from lxml import etree
import json
import time


class tourist_routes(object):
    def __init__(self):
        self.page = 1
        self.url = 'https://vacations.ctrip.com/list/whole/sc1.html?filter=dc1&p=' + str(self.page) + '&s=2&st=%E9%BB%84%E5%B1%B1&startcity=1&sv=%E9%BB%84%E5%B1%B1'
        self.option = webdriver.ChromeOptions()
        '''
        self.option.add_argument('--headless')
        self.option.add_argument('--no-sandbox')
        self.option.add_argument('--disable-dev-shm-usage')
        self.option.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=self.option, executable_path='/usr/local/bin/chromedriver')
        '''
        self.driver = webdriver.Chrome(options=self.option)
        self.routes_num = 0

    def get_data(self):
        """
        进入页面
        :return:本页页面data
        """

        self.driver.get(self.url)

        # 等待5秒，等待网页相应
        time.sleep(5)

        # 点击下一页，再点击上一页，防止携程反爬
        self.driver.execute_script('var q=document.documentElement.scrollTop=10000')
        self.driver.find_element_by_class_name('down').click()
        # 等待5秒，等待网页相应
        time.sleep(5)
        self.driver.execute_script('var q=document.documentElement.scrollTop=10000')
        self.driver.find_element_by_class_name('up').click()
        # 等待5秒，等待网页相应
        time.sleep(5)

        # 模拟页面滚动,确保数据加载完毕
        self.driver.execute_script('var q=document.documentElement.scrollTop=10000')

        '''
        # 点击统一选择“北京出发”
        if self.url == 'https://vacations.ctrip.com/list/whole/sc1.html?p=1&st=%E4%B8%89%E4%BA%9A&startcity=1&sv=%E4%B8%89%E4%BA%9A':
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div[1]/div[2]/div[2]/div/div/span[1]').click()
            # 等待3秒，等待网页相应
            time.sleep(3)

        # 点击销量优先
        if self.url == 'https://vacations.ctrip.com/list/whole/sc1.html?p=1&st=%E4%B8%89%E4%BA%9A&startcity=1&sv=%E4%B8%89%E4%BA%9A':
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[6]/div/div[1]/span[2]').click()
            # 等待3秒，等待网页相应
            time.sleep(3)
        '''

        # 获得网页数据
        data = self.driver.page_source

        return data

    def parse_data(self, data):
        """
        解析，提取数据
        :param data: 本页网页data
        :return: 本页数据
        """

        # 创建最外层list
        data_list = []

        # 获取、解析
        html = etree.HTML(data)
        node_list = html.xpath('//div[@class="list_product_item_border"]')
        for node in node_list:

            try:
                # 创建每条线路的字典
                temp = {}

                # 获取线路名
                temp['线路名'] = node.xpath('./div/div[2]/p/span/text()')[0]
                print(temp['线路名'])

                # 获取编号，拼接生成详情页url
                id_list = node.xpath('./parent::div[@class="list_product_box js_product_item"]/@data-track-product-id')
                for id in id_list:
                    temp['编号'] = int(id)
                    detail_url = 'https://vacations.ctrip.com/travel/detail/p' + id + '/?city=1'
                    print(detail_url)
                    temp['url'] = detail_url

                # 获取描述信息
                temp['描述信息'] = node.xpath('./div/div[2]/div/div[2]/div[2]/div/p/text()')[0]

                # 获取供应商
                supplier = node.xpath('./div/div[2]/div/div[2]/p//text()')
                if len(supplier) == 1:
                    temp['供应商'] = supplier[0].split("：")[1]
                else:
                    temp['供应商'] = supplier[2]

                try:
                    # 进入详情页
                    opt = webdriver.ChromeOptions()
                    opt.add_argument('--headless')
                    '''
                    opt.add_argument('--no-sandbox')
                    opt.add_argument('--disable-dev-shm-usage')
                    opt.add_argument('--disable-gpu')
                    driver1 = webdriver.Chrome(options=opt, executable_path='/usr/local/bin/chromedriver')
                    '''
                    driver1 = webdriver.Chrome(options=opt)
                    driver1.get(detail_url)
                    # 等待4秒，等待网页相应
                    time.sleep(4)
                except:
                    try:
                        # 再次尝试进入详情页
                        opt = webdriver.ChromeOptions()
                        opt.add_argument('--headless')
                        '''
                        opt.add_argument('--no-sandbox')
                        opt.add_argument('--disable-dev-shm-usage')
                        opt.add_argument('--disable-gpu')
                        driver1 = webdriver.Chrome(options=opt, executable_path='/usr/local/bin/chromedriver')
                        '''
                        driver1 = webdriver.Chrome(options=opt)
                        driver1.get(detail_url)
                        # 等待4秒，等待网页相应
                        time.sleep(4)
                    except:
                        print('2次尝试已完成，未进入详情页，此条线路跳过')
                        continue
                    else:
                        # 已进入详情页
                        # 模拟页面滚动
                        driver1.execute_script('var q=document.documentElement.scrollTop=10000')
                        # 等待2秒，等待网页相应
                        time.sleep(2)

                        # 获取、解析详情页
                        detail_page = driver1.page_source
                        hr = etree.HTML(detail_page)

                        # 获取钻数评级
                        temp['钻数'] = len(driver1.find_elements_by_class_name('product_diamond'))

                        # 获取简介
                        temp['简介'] = hr.xpath('//*[@id="base_bd"]/div[1]/div/div[2]/div[1]/p/text()')

                        # 获取卖点
                        features = driver1.find_element_by_class_name('pm_rec')
                        temp['卖点'] = []
                        for feature in features.find_elements_by_xpath('.//li'):
                            temp['卖点'].append(feature.text.split(" ")[1])

                        # 获取行程
                        temp['行程'] = hr.xpath('//div[@class="day_title"]/div[2]/text()')

                        # 获取酒店
                        temp['酒店'] = hr.xpath('//a[@class="itinerary_hotel_item js_Expose_Point js_mapPointHook"]/text()')

                        # 获取总评分
                        temp['总评分'] = hr.xpath(
                            '//*[@id="js_Review"]/div/div/div[1]/div/div[2]/div[1]/div[2]/span[1]/text()')

                        # 获取好评率
                        temp['好评率'] = hr.xpath(
                            '//*[@id="js_Review"]/div/div/div[1]/div/div[2]/div[1]/div[3]/span/text()[1]')

                        # 获取各项评分
                        list_marks = hr.xpath('//*[@id="js_Review"]/div/div/div[1]/div/div[2]/div[2]//text()')
                        temp['各项评分'] = {}
                        for i in range(0, len(list_marks), 2):
                            temp['各项评分'][list_marks[i]] = float(list_marks[i + 1])

                        # 获取关键词
                        key_words = hr.xpath('//*[@id="js_Review"]/div/div/div[1]/div/div[3]/div[2]/div/text()')
                        temp['关键词'] = []
                        for key_word in key_words:
                            key_word = key_word.split(" ")[0]
                            # 筛去无意义的关键词
                            if key_word == '全部':
                                continue
                            elif key_word == '好评':
                                continue
                            elif key_word == '中评':
                                continue
                            elif key_word == '差评':
                                continue
                            elif key_word == '有图':
                                continue
                            elif key_word == '追评':
                                continue
                            else:
                                temp['关键词'].append(key_word)

                        # 获取评论
                        # 评论的一些基本信息
                        users = hr.xpath(
                            '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[1]/p/text()')
                        mates = hr.xpath(
                            '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/ul/li[1]/p/text()')
                        times = hr.xpath(
                            '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/ul/li[2]/p/text()')
                        marks = driver1.find_elements_by_class_name('ct-review-text-1')
                        comments = hr.xpath(
                            '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div/div[2]/p/text()')
                        # 构建需要的格式
                        comment = []
                        for i in range(0, len(comments)):
                            com = {'用户名': users[i], '同行': mates[i], '时间': times[i].split(" ")[0], '用户评分': marks[i].text,
                                   '评论': comments[i]}
                            comment.append(com)
                        temp['评论'] = comment

                        # 获取价格
                        try:
                            try:
                                try:
                                    price = driver1.find_element_by_xpath(
                                        '//*[@id="base_bd"]/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[2]/span/em').text
                                except:
                                    try:
                                        price = driver1.find_element_by_xpath(
                                            '//*[@id="base_bd"]/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/span/em').text
                                    except:
                                        try:
                                            price = driver1.find_element_by_xpath(
                                                '//*[@id="base_bd"]/div[1]/div/div[3]/div[1]/div[1]/div[1]/div[2]/span/em').text
                                        except:
                                            print('未知价格路径，跳过此条线路')
                                            price = -1
                                            temp['价格'] = price
                            except:
                                print('根本不会到这，什么也没发生')
                        except:
                            print('根本不会到这，什么也没发生')
                        finally:
                            if price == '实时计价':
                                temp['价格'] = -1
                            else:
                                temp['价格'] = int(price)

                        data_list.append(temp)

                        driver1.quit()

                        self.routes_num = self.routes_num + 1
                        print(self.routes_num)
                else:
                    # 已进入详情页
                    # 模拟页面滚动
                    driver1.execute_script('var q=document.documentElement.scrollTop=10000')
                    # 等待2秒，等待网页相应
                    time.sleep(2)

                    # 获取、解析详情页
                    detail_page = driver1.page_source
                    hr = etree.HTML(detail_page)

                    # 获取钻数评级
                    temp['钻数'] = len(driver1.find_elements_by_class_name('product_diamond'))

                    # 获取简介
                    temp['简介'] = hr.xpath('//*[@id="base_bd"]/div[1]/div/div[2]/div[1]/p/text()')

                    # 获取卖点
                    features = driver1.find_element_by_class_name('pm_rec')
                    temp['卖点'] = []
                    for feature in features.find_elements_by_xpath('.//li'):
                        temp['卖点'].append(feature.text.split(" ")[1])

                    # 获取行程
                    temp['行程'] = hr.xpath('//div[@class="day_title"]/div[2]/text()')

                    # 获取酒店
                    temp['酒店'] = hr.xpath('//a[@class="itinerary_hotel_item js_Expose_Point js_mapPointHook"]/text()')

                    # 获取总评分
                    temp['总评分'] = hr.xpath('//*[@id="js_Review"]/div/div/div[1]/div/div[2]/div[1]/div[2]/span[1]/text()')

                    # 获取好评率
                    temp['好评率'] = hr.xpath('//*[@id="js_Review"]/div/div/div[1]/div/div[2]/div[1]/div[3]/span/text()[1]')

                    # 获取各项评分
                    list_marks = hr.xpath('//*[@id="js_Review"]/div/div/div[1]/div/div[2]/div[2]//text()')
                    temp['各项评分'] = {}
                    for i in range(0, len(list_marks), 2):
                        temp['各项评分'][list_marks[i]] = float(list_marks[i + 1])

                    # 获取关键词
                    key_words = hr.xpath('//*[@id="js_Review"]/div/div/div[1]/div/div[3]/div[2]/div/text()')
                    temp['关键词'] = []
                    for key_word in key_words:
                        key_word = key_word.split(" ")[0]
                        # 筛去无意义的关键词
                        if key_word == '全部':
                            continue
                        elif key_word == '好评':
                            continue
                        elif key_word == '中评':
                            continue
                        elif key_word == '差评':
                            continue
                        elif key_word == '有图':
                            continue
                        elif key_word == '追评':
                            continue
                        else:
                            temp['关键词'].append(key_word)

                    # 获取评论
                    # 评论的一些基本信息
                    users = hr.xpath(
                        '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[1]/p/text()')
                    mates = hr.xpath(
                        '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/ul/li[1]/p/text()')
                    times = hr.xpath(
                        '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/ul/li[2]/p/text()')
                    marks = driver1.find_elements_by_class_name('ct-review-text-1')
                    comments = hr.xpath(
                        '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div/div[2]/p/text()')
                    # 构建需要的格式
                    comment = []
                    for i in range(0, len(comments)):
                        com = {'用户名': users[i], '同行': mates[i], '时间': times[i].split(" ")[0], '用户评分': marks[i].text,
                               '评论': comments[i]}
                        comment.append(com)
                    temp['评论'] = comment

                    # 获取价格
                    try:
                        try:
                            try:
                                price = driver1.find_element_by_xpath(
                                    '//*[@id="base_bd"]/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[2]/span/em').text
                            except:
                                try:
                                    price = driver1.find_element_by_xpath(
                                        '//*[@id="base_bd"]/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/span/em').text
                                except:
                                    try:
                                        price = driver1.find_element_by_xpath(
                                            '//*[@id="base_bd"]/div[1]/div/div[3]/div[1]/div[1]/div[1]/div[2]/span/em').text
                                    except:
                                        print('未知价格路径，跳过此条线路')
                                        price = -1
                                        temp['价格'] = price
                        except:
                            print('根本不会到这，什么也没发生')
                    except:
                        print('根本不会到这，什么也没发生')
                    finally:
                        if price == '实时计价':
                            temp['价格'] = -1
                        else:
                            temp['价格'] = int(price)

                    data_list.append(temp)

                    driver1.quit()

                    self.routes_num = self.routes_num + 1
                    print(self.routes_num)
            except:
                print('报错，跳过此条线路')
                continue

        return data_list

    def next_page(self):
        """
        翻页
        :return: 下一页的URL
        """
        if self.page == 43:
            print('！！！1-43（共）爬取完毕！！！')
            return None
        else:
            self.page = self.page + 1
            next_url = 'https://vacations.ctrip.com/list/whole/sc1.html?filter=dc1&p=' + str(self.page) + '&s=2&st=%E9%BB%84%E5%B1%B1&startcity=1&sv=%E9%BB%84%E5%B1%B1'
            self.url = next_url
            print('新一页的url：' + self.url)
            print('正在爬取第 ' + str(self.page) + ' 页：')
            return self.url

    def save_data(self, data_list):
        """
        保存数据，一页保存一次
        :param data_list: 刚刚爬取的页面数据
        :return: None
        """
        for i in data_list:
            data = json.dumps(i, indent=4, ensure_ascii=False)
            with open('黄山.json', 'a', encoding='utf8') as f:
                data = str(data) + ',\n'
                f.write(data)
                f.close()
        print('-------------第 ' + str(self.page) + ' 页已写入文件-------------')

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
            if id == None:
                break
        self.driver.quit()


if __name__ == '__main__':
    spider_routes = tourist_routes()
    spider_routes.run()
