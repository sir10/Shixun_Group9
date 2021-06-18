import glob
import os
import random
import re
from time import time

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from gensim.models import LdaModel
from gensim.corpora import Dictionary
import matplotlib.pyplot as plt

word_tensor_paths = glob.glob('.\\tensor\\*.txt')
data = []
data_split = []
for word_tensor_path in word_tensor_paths[21:]:

    # 城市名
    city_name = re.split('[._]', word_tensor_path.split('\\')[-1])[0]
    # 获取训练数据
    with open(word_tensor_path, 'r', encoding='utf-8') as f:
        text_data = f.read().split('\n')
        for text_item in text_data:
            words = []
            for word in text_item.split():
                if len(word) > 1:
                    words.append(word)
            data_split.append(words)
            data.append(' '.join(data_split[-1]))

    # 创建困惑度目录
    if not os.path.exists('./lda/perplexity/{}'.format(city_name)):
        os.mkdir('./lda/perplexity/{}'.format(city_name))

    # 计算困惑度，获得最合适聚类个数
    bow_corpus = []
    for trace in data:
        bow_corpus.append(trace)
    # 分解训练集和测试集
    train_size = int(round(len(bow_corpus) * 0.8))
    # 随机选取下标
    train_index = sorted(random.sample(range(len(bow_corpus)), train_size))
    test_index = sorted(set(range(len(bow_corpus))) - set(train_index))
    train_corpus = [bow_corpus[i] for i in train_index]
    test_corpus = [bow_corpus[j] for j in test_index]

    n_features = 2000
    n_top_words = 1000

    print("Extracting tf features for LDA...")
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=n_features)  ###选取至少出现过两次并且数量为前2000的单词用来生成文本表示向量
    t0 = time()
    tf = tf_vectorizer.fit_transform(train_corpus)  ###使用向量生成器转化测试集
    print("done in %0.3fs." % (time() - t0))
    # Use tf (raw term count) features for LDA.
    print("Extracting tf features for LDA...")
    tf_test = tf_vectorizer.transform(test_corpus)
    print("done in %0.3fs." % (time() - t0))
    grid = dict()
    t0 = time()
    min_perplexity = 9999
    min_perplexity_topics = 0
    # 40个主题，以2为间隔
    for i in range(1, 40, 2):
        grid[i] = list()
        n_topics = i

        # 定义lda模型
        lda = LatentDirichletAllocation(n_components=n_topics, max_iter=5, learning_method='online',
                                        learning_offset=50., random_state=0)
        # 训练参数
        lda.fit(tf)
        # 得到topic-document 分布
        train_gamma = lda.transform(tf)
        # train_perplexity = lda.perplexity(tf)
        # 计算测试集困惑度
        test_perplexity = lda.perplexity(tf_test)
        print('sklearn preplexity: test=%.3f' % (test_perplexity))

        grid[i].append(test_perplexity)
        if test_perplexity < min_perplexity:
            min_perplexity = test_perplexity
            min_perplexity_topics = i

    print("done in %0.3fs." % (time() - t0))

    df = pd.DataFrame(grid)
    df.to_csv('./lda/perplexity/{}/sklearn_perplexity.csv'.format(city_name))
    print(df)
    plt.figure(figsize=(14, 8), dpi=120)
    # plt.subplot(221)
    plt.plot(df.columns.values, df.iloc[0].values, '#007A99')
    plt.xticks(df.columns.values)
    plt.ylabel('test Perplexity')
    plt.savefig('./lda/perplexity/{}/lda_topic_perplexity.png'.format(city_name), bbox_inches='tight', pad_inches=0.1)
    # plt.show()

    # 文本向量化
    dictionary = Dictionary(data_split)
    dictionary.filter_n_most_frequent(200)
    corpus = [dictionary.doc2bow(text) for text in data_split]

    # LDA 模型训练
    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=min_perplexity_topics)

    # 获取主题分布
    topic_list = lda.print_topics(num_topics=min_perplexity_topics, num_words=10)

    print(topic_list)

    with open('./lda/topics/{}_topics.txt'.format(city_name), 'w', encoding='utf-8') as file_topics:
        for topic_item in topic_list:
            file_topics.write(str(topic_item[0]) + ',' + topic_item[1] + '\n')