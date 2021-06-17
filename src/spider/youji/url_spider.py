import json
import re
from time import sleep
import fake_useragent
import requests
from pyasn1.compat.octets import null
from bs4 import BeautifulSoup
user_agent = fake_useragent.UserAgent()
# print(user_agent.random)

headers = {
            'user-agent': user_agent.random
        }

# 提取代理API接口，获取1个代理IP
api_url = "https://dps.kdlapi.com/api/getdps/?orderid=902311786136931&num=1&pt=1&dedup=1&sep=1"

# 获取API接口返回的代理IP
proxy_ip = requests.get(api_url).text

# 用户名密码认证(私密代理/独享代理)
username = "100245"
password = "100245"
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
}

# site_list = []
# site_url = 'https://you.ctrip.com/sitelist/china110000.html'
# list_url = 'https://you.ctrip.com/travels/changbaishan268/t3-p2.html'
base_detail_url = 'https://gs.ctrip.com/html5/you/travels/'
list_payload = {"Keyword": "", "PoiId": "", "DistrictId": "1", "PageSize": 50, "PageIndex": 1, "PhotoWidth": 240,
                "PhotoHeight": 274, "TravelMonth": "", "CompanionTypeList": "", "RecommendTypeList": "",
                "TravelDaysMin": -1, "TravelDaysMax": -1, "OrderByField": 2, "TemplateVersion": 2,
                "contentType": "json"}

# site_response = requests.get(site_url, headers=headers)
# site_text = BeautifulSoup(site_response.text, 'lxml')
# site_elements = site_text.select('div.hot_destlist > ul > li > a') + site_text.select('ul.c_city_nlist > li > a')
# for site_element in site_elements:
#     site_name = site_element.get('href').split('/')[-1].split('.')[0]
#     site_num = re.findall('\d+', site_name)[0]
#     site_name = site_name.replace(site_num, '')
#     site_list.append({site_name: site_num})
#     # print(site_name, site_num)
# with open('city_list.json', 'w', encoding='utf-8') as f1:
#     json.dump(site_list, f1, ensure_ascii=False, indent=4)

site_list = [
    {
        "sanya": "61"
    },
    {
        "guilin": "28"
    },
    {
        "xian": "7"
    },
    {
        "huangshan": "120061"
    },
    {
        "jiuzhaigou": "25"
    },
    {
        "hulunbeier": "458"
    },
    {
        "zhangjiajie": "23"
    },
    {
        "qingdao": "5"
    },
    {
        "lhasa": "36"
    }
]
base_list_url = 'https://you.ctrip.com/travels/'
# print(site_list)
# print(site_dict.keys())

for site_dict in site_list:
    k = ''
    for key in site_dict.keys():
        k = key
    list_url = base_list_url + k + site_dict[k] + '.html'
    page_response = requests.get(list_url, headers=headers)
    page_text = BeautifulSoup(page_response.text, 'lxml')
    page_num = int(page_text.select('div.pager_v1 > span > b.numpage')[0].get_text())
    if page_num > 500:
        page_num = 500
    page_response.close()
    youji_data = []
    url_data = []
    list_urls = [base_list_url + k + site_dict[k] + '/t3-p{}.html'.format(str(i)) for i in range(1, page_num+1)]
    # list_payload['DistrictId'] = k
    print('开始爬取 {} 的游记内容......'.format(k))
    for list_url_item in list_urls:
        # print('页面{}/500......'.format(str(i)))
        # list_payload['PageIndex'] = i
        list_response = requests.get(list_url_item, headers=headers)
        list_response_text = BeautifulSoup(list_response.text, 'lxml')
        list_youji_elements = list_response_text.select('a.journal-item')
        # if list_youji is None:
        #     break
        # print(len(list_youji))
        # j = 0
        for item in list_youji_elements:
            url = item.get('href')
            print(url)
            url_data.append(url)
        list_response.close()
        sleep(1)
    with open('./url/{}_url.txt'.format(k), 'w', encoding='utf-8') as f:
        for item in url_data:
            f.write(item + '\n')
        print('{}_url.txt生成完成！！！'.format(k))
        # sleep(1)
    # sleep(10)
    #     youji_element = item
    #     detail_url = base_detail_url + site_dict[k] + '/' + str(youji_element['Id']) + '.html'
    #     detail_response = requests.get(detail_url, headers=headers)
    #     detail = detail_response.text
    #     detail_elements = BeautifulSoup(detail, 'lxml')
    #     content = detail_elements.select('div.travels_detail')[0]
    #     content_str = content.get_text().replace(' ', '').strip()
    #     youji_element['content'] = content_str
    #     youji_data.append(youji_element)
    #     j = j + 1
    #     print('----- {}/10 -----'.format(str(j)))
    #     if j % 5 == 0:
    #         print('...... 休息 2 s ......')
    #         sleep(2)

    # with open(k + '_youji.json', 'w', encoding='utf-8') as f:
    #     json.dump(youji_data, f, ensure_ascii=False, indent=4)
    # print('文件{}.json生成完成！！！！'.format(k))
    # sleep(10)
    #牛啊