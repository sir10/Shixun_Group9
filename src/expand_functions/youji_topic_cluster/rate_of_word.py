import glob
import re
import pandas as pd

word_tensor_paths = glob.glob('.\\tensor\\*.txt')
data = []

for word_tensor_path in word_tensor_paths:

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
        sight_rate_format.append({'sight_name': k, 'count': v})

    # 存入文件
    df = pd.DataFrame(sight_rate_format)
    print(df)
    df.to_csv('./sight_word/sight_word_rate/{}.csv'.format(city_name), encoding='utf-8_sig')
    print('------ 存取{}.csv成功！！！！！------'.format(city_name))
