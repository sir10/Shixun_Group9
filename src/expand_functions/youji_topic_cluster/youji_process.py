import glob
import json
import os
import re
import jieba
import jieba.posseg


# 提取自定义词库
# sight_paths = glob.glob('.\\ticket_url\\*.json')
# for sight_path in sight_paths:
#     city_name = sight_path.split('\\')[-1].split('.')[0]
#     sight_list = json.load(open(sight_path, 'r', encoding='utf-8'))
#
#     sight_name_list = [item['name'] for item in sight_list]
#     with open('./sight_word/{}_sight_word.txt'.format(city_name), 'w', encoding='utf-8') as sight:
#         for sight_name in sight_name_list:
#             sight.write(sight_name + '\n')

# 停用词表
stopwords = []
stopword_paths = glob.glob('.\\stopword\\*.txt')
for stopword_path in stopword_paths:
    with open(stopword_path, 'r', encoding='utf-8') as stopword_file:
        lines = stopword_file.read().split('\n')
        for line in lines:
            if line not in stopwords:
                stopwords.append(line)


city_list = os.listdir('./youji')
for city in city_list:
    # 景点名称
    sight_word_list = []
    with open('./sight_word/{}_sight_word.txt'.format(city), 'r', encoding='utf-8') as sight:
        lines = sight.read().split('\n')
        for l in lines:
            sight_word_list.append(l)

    # 获取游记文本地址
    youji_content_urls = glob.glob('.\\youji\\{}\\*.txt'.format(city))

    # sight_rate_dict = {}

    word_tensor_list = []

    # 逐个处理
    for youji_content_url in youji_content_urls:

        # 加载游记文本主体
        with open(youji_content_url, 'r', encoding='utf-8') as f:
            content = f.read()

        # 去除链接
        link = re.compile(r'http://[a-zA-Z0-9.?/&=:]*', re.S)
        content = link.sub('', content)

        # 导入地点词典
        jieba.load_userdict('./sight_word/{}_sight_word.txt'.format(city))

        # 分词, 且仅保留名词、形容词、景点名词
        seg_list = jieba.posseg.cut(content.strip())
        seg_list_out = []
        for seg in seg_list:
            if seg.flag[0] == 'n' or seg.flag[0] == 'a' or seg.word in sight_word_list:
                seg_list_out.append(seg)

        # 去停用词
        word_list = []
        for seg in seg_list_out:
            if seg.word not in stopwords:
                word_list.append(seg.word)
        youji_url_segs = youji_content_url.split('/')

        # 存入向量list
        word_tensor_list.append(word_list)

        # 写入向量文件中
        with open('./tensor/{}_tensor.txt'.format(city), 'a', encoding='utf-8') as extract_file:
            extract_file.write(' '.join(word_list))
            extract_file.write('\n')
    print('{}_tensor 已生成！！！'.format(city))




    # print(sight_rate_dict)

