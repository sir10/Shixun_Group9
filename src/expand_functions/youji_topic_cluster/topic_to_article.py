# -*- coding: utf-8 -*-
import glob
import json
import math
import os
import re

import numpy as np

# 语料库
filenames = glob.glob('.\\tensor\\*.txt')


def get_dic_input(input_dict):
    length_input = len(input_dict.keys())
    for key in input_dict.keys():
        input_dict[key] = 0

    return input_dict, length_input


def get_tf_idf(topic_dict, file_name):
    dic_input_idf, length_input = get_dic_input(topic_dict)

    f = open(file_name, 'r', encoding='utf-8')
    list_tf = []
    list_idf = []
    word_vector1 = np.zeros(length_input)
    word_vector2 = np.zeros(length_input)

    lines = f.read().split('\n')
    length_essay = len(lines)
    f.close()

    # 计算出每个词的idf值依次存储在list_idf中
    for key in dic_input_idf:
        for line in lines:
            if key in line.split():
                dic_input_idf[key] += 1
        list_idf.append(math.log(length_essay / (dic_input_idf[key] + 1)))

    # 将idf值存储在矩阵向量中
    for i in range(length_input):
        word_vector1[i] = list_idf.pop()

    # 依次计算每个词在每行的tf值依次存储在list_tf中
    index = 0
    data = {}
    for line in lines:
        if line == '':
            continue
        length = len(line.split())
        dic_input_tf, length_input = get_dic_input(topic_dict)

        for key in line.split():
            if key in dic_input_tf:
                dic_input_tf[key] += 1
        for key in dic_input_tf:
            tf = dic_input_tf[key] / length
            list_tf.append(tf)

        # 将每行tf值存储在矩阵向量中
        for i in range(length_input):
            word_vector2[i] = list_tf.pop()

        # print(word_vector2)
        # print(word_vector1)
        tf_idf = float(np.sum(word_vector2 * word_vector1))
        # 筛选出相似度高的文章
        # if tf_idf > 0.1:
            # print("tf_idf值：", tf_idf)
            # print("文章id：", index)
        data[str(index)] = tf_idf
        index += 1

    return data

if os.path.exists('./lda/topic_youji.json'):
    topic_youji_total = json.load(open('./lda/topic_youji.json', 'r', encoding='utf-8'))
else:
    topic_youji_total = {}

for filename in filenames[13:]:

    # 获取主题文件路径
    city_name = re.split('[._]', filename.split('\\')[-1])[0]
    topic_path = './lda/topics/{}_topics.txt'.format(city_name)

    # 读取topic文件
    topics_text = []
    with open(topic_path, 'r', encoding='utf-8') as topic_file:
        topics_text = [topic_element.split(',')[-1].split(' + ') for topic_element in topic_file.read().split('\n')]

    id_list = []
    for topic_element in topics_text:
        topic_dict = {}
        for topic_item in topic_element:
            topic_item_tuple = topic_item.replace('"', '').split('*')
            topic_dict[topic_item_tuple[1]] = topic_item_tuple[0]

        # 获取相关游记的相关度信息
        relative_data = get_tf_idf(topic_dict, filename)
        max_tf_idf = max(relative_data.values())
        max_relative_data_id = -1
        for k in relative_data.keys():
            if relative_data[k] == max_tf_idf:
                id_list.append(k)
                break

    # 获取游记内容
    topic_youji = []
    youji_json = json.load(open('./youji_detail/{}_youji.json'.format(city_name), 'r', encoding='utf-8'))
    for id in id_list:
        max_relative_youji = youji_json[int(id)]
        topic_youji.append({
            'title': max_relative_youji['title'],
            'content': max_relative_youji['content'],
            'like': max_relative_youji['like'],
            'comments': max_relative_youji['comments'],
            'url': max_relative_youji['url']
        })

    topic_youji_total[city_name] = topic_youji
    print(city_name + ' finish!!!')
    # 写入json中
    with open('./lda/topic_youji.json', 'w', encoding='utf-8') as total_file:
        json.dump(topic_youji_total, total_file, ensure_ascii=False, indent=4)