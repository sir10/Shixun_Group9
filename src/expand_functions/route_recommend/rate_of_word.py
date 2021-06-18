import glob
import json
import random
import re
import pandas as pd

word_tensor_paths = glob.glob('.\\tensor\\*.txt')
data = []

# 权重生成函数
def get_weight(count, rank):
    if rank in range(1, 21):
        rank_score = 1-0.001*rank
    elif rank in range(21, 51):
        rank_score = 0.98-0.005*(rank-20)
    elif rank in range(51, 101):
        rank_score = 0.83-0.01*(rank-50)
    elif rank in range(101, 501):
        rank_score = 0.33
    else:
        rank_score = 0.1

    return count * rank_score

for word_tensor_path in word_tensor_paths[20:]:

    # 城市名
    city_name = re.split('[._]', word_tensor_path.split('\\')[-1])[0]

    # 获取文本数据
    with open(word_tensor_path, 'r', encoding='utf-8') as f:
        text_data = f.read().split('\n')
        for text_item in text_data:
            words = []
            for word in text_item.split():
                if len(word) > 1:
                    words.append(word)
            data.append(words)
    print('------ 获取{}_youji 成功！！！！！------'.format(city_name))

    # 导入景点词典
    sight_word_list = []
    with open('./sight_word/{}_sight_word.txt'.format(city_name), 'r', encoding='utf-8') as sight:
        lines = sight.read().split('\n')
        for l in lines:
            sight_word_list.append(l)
    print('------ 导入{}_sight 成功！！！！！------'.format(city_name))

    # 统计景点词频
    sight_rate_dict = {}
    for words in data:
        for word in words:
            if word in sight_word_list:
                if word in sight_rate_dict:
                    sight_rate_dict[word] += 1
                else:
                    sight_rate_dict[word] = 1

    sight_rate_format = []
    for k, v in sight_rate_dict.items():

        # 计算权重
        rank = sight_word_list.index(k) + 1
        weight = get_weight(v, rank)

        # 存入格式化list
        sight_rate_format.append({'sight_name': k, 'count': v, 'weight': weight})

    # 获取推荐线路
    df = pd.DataFrame(sight_rate_format)
    df.sort_values(by=['weight'], ascending=False, inplace=True)
    list_recommend = df.head(10)['sight_name']
    recommend_route = '+'.join(list_recommend)
    print(recommend_route)


    # 获取真实线路3条
    cluster_id = random.choices(range(6), k=3)
    route_id = random.choices(range(10), k=3)
    real_routes = []

    if city_name == 'beijing':
        real_routes = [{'name': '古北水镇2日自由行·携程自营·万人选择·指定宿古北之光·赠温泉票+特色午餐‖无限次水镇进出门票+电瓶车‖含市区-景区巴士‖观无人机表演+超炫3D水舞秀‖可选司马台&游船（自选）',
                        'url': 'https://vacations.ctrip.com/travel/detail/p15627504/?city=1'},
                       {'name': '北京5日4晚私家团·周五出发·指定丽思卡尔顿  一线国际 索菲特/诺金/丽思卡尔顿｜故宫通票·4小时，八达岭/慕田峪长城二选一，恭王府/雍和宫任选;『皇城特色』提前7天预订，赠黄包车游胡同，感受老北京风情',
                        'url': 'https://vacations.ctrip.com/travel/detail/p20856545/?city=1'},
                       {'name': '北京5日4晚私家团·【亲子私家游·一线国际5 威斯汀/喜来登/诺金酒店】1单1团，人多优惠多，跟着课本探秘中国科技馆+清华入内参观+童趣什刹海，故宫深度5H，体验大不同，专车专导轻松游，24H接送',
                        'url': 'https://vacations.ctrip.com/travel/detail/p29924403/?city=1'}]
    else:
        routes = json.load(open('./routes/{}.json'.format(city_name), 'r', encoding='utf-8'))
        for i in cluster_id:
            for j in route_id:
                route = routes[i]['tourist_route'][j]
                real_routes.append({'name': route['route_name'],
                                    'url': route['url']})

    route_list = [{
        'recommend_route': recommend_route,
        'real_route': real_routes
    }]
    with open('./routes/{}.json'.format(city_name), 'w', encoding='utf-8') as route_json:
        json.dump(route_list, route_json, ensure_ascii=False, indent=4)
    # df.to_csv('./sight_word/sight_word_rate/{}.csv'.format(city_name), encoding='utf-8_sig')
    print('------ 存取{}.json成功！！！！！------'.format(city_name))
