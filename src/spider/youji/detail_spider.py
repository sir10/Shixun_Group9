# -*- coding: utf-8 -*-
import json
import re
from glob import glob
from time import sleep
import os
from bs4 import BeautifulSoup
import fake_useragent
import requests

# 提取代理API接口，获取1个代理IP
from pyasn1.compat.octets import null

# api_url = "https://dps.kdlapi.com/api/getdps/?orderid=902311786136931&num=1&pt=1&dedup=1&sep=1"
#
# # 获取API接口返回的代理IP
# proxy_ip = requests.get(api_url).text
#
# # 用户名密码认证(私密代理/独享代理)
# username = "100245"
# password = "100245"
# proxies = {
#     "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
#     "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
# }

user_agent = fake_useragent.UserAgent()

headers = {
    'user-agent': user_agent.random
}

url_text_paths = glob('.\\url_format\\*.txt')

for url_text_path in url_text_paths:
    url_list = []
    # 读取全部url
    with open(url_text_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            url_list.append(line)

    city_name = re.split('[._]', url_text_path.split('\\')[-1])[0]
    path = './youji_detail/{}_youji.json'.format(city_name)
    if os.path.exists(path):
        city_youji_data = json.load(open('./youji_detail/{}_youji.json'.format(city_name), 'r', encoding='utf-8'))
    else:
        city_youji_data = []

    i = 0

    for url_item in url_list:
        detail_response = requests.get(url_item, headers=headers)
        detail_text = BeautifulSoup(detail_response.text, 'lxml')
        youji_data = {
            'title': detail_text.select('div.cover-content > div.title > h1')[0].get_text() if len(detail_text.select('div.cover-content > div.title > h1')) > 0 else '',
            'start_date': detail_text.select('div.arrangement > div.start_date')[0].get_text() if len(detail_text.select('div.arrangement > div.start_date')) > 0 else '',
            'out_day': detail_text.select('div.arrangement > div.out_days')[0].get_text() if len(detail_text.select('div.arrangement > div.out_days')) > 0 else '',
            'whom_with': detail_text.select('div.arrangement > div.whom_with')[0].get_text() if len(detail_text.select('div.arrangement > div.whom_with')) > 0 else '',
            'aver_cost': detail_text.select('div.cover-content > div.arrangement > div.aver_cost')[0].get_text() if len(detail_text.select('div.cover-content > div.arrangement > div.aver_cost')) > 0 else '',
            'content': detail_text.select('div.travels_detail')[0].get_text().strip() if len(detail_text.select('div.travels_detail')) > 0 else '',
            'like': detail_text.select('#c_good')[0].get_text().split()[-1] if len(detail_text.select('#c_good')) > 0 else '0',
            'comments': detail_text.select('#c_comments')[0].get_text().split()[-1] if len(detail_text.select('#c_comments')) > 0 else '0',
            'url': url_item
        }
        detail_response.close()
        city_youji_data.append(youji_data)
        i += 1
        print(youji_data)
        sleep(1)
        if i % 100 == 0:
            with open('./youji_detail/{}_youji.json'.format(city_name), 'w', encoding='utf-8') as f:
                json.dump(city_youji_data, f, ensure_ascii=False, indent=4)
    print('------ {}'.format(city_name) + '游记爬取完成！！！ ------')

    with open('./youji_detail/{}_youji.json'.format(city_name), 'w', encoding='utf-8') as f:
        json.dump(city_youji_data, f, ensure_ascii=False, indent=4)

    # print('------ 文件{}_youji.json'.format(city_name) + '生成完成！！！ ------')

