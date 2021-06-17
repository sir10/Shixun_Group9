from numpy import *
from nltk.cluster.util import cosine_distance


def cosDistance(vector1, vector2):
    """
    使用余弦相似度代替传统k-means的欧氏距离。
    欧氏距离衡量的是空间各点的绝对距离；而余弦距离衡量的是空间向量的夹角，更加体现在方向上的差异，而不是位置。
    如果保持 A 点位置不变，B 点朝原方向远离坐标轴原点，那么这个时候余弦距离是保持不变的（因为夹角没有发生变化），而 A 与 B 两点的距离显然在发生变化，这就是欧式距离与余弦相似度的不同之处。
    :param vector1: 向量1
    :param vector2: 向量2
    :return: 向量1、2的余弦相似度
    """
    return cosine_distance(vector1, vector2)


def initCentroids(dataSet, k):
    """
    使用随机样例初始化质心
    :param dataSet: 要被聚类的数据集
    :param k: 聚类个数
    :return: 被初始化的聚类中心点的坐标list
    """
    # k是指用户设定的k个种子点
    # dataSet - 此处为mat对象
    numSamples, dim = dataSet.shape
    # numSample - 行，此处代表数据集数量  dim - 列，此处代表维度，例如只有xy轴的，dim=2
    centroids = zeros((k, dim))  # 产生k行，dim列零矩阵
    for i in range(k):
        index = int(random.uniform(0, numSamples))  # 给出一个服从均匀分布的在0~numSamples之间的整数
        centroids[i, :] = dataSet[index, :]  # 第index行作为种子点（质心）
    return centroids


def kmeans(dataSet, k):
    """
    实现基于余弦相似度的kmeans
    :param dataSet: 要被聚类的数据集
    :param k: 聚类个数
    :return: centroids:聚类中心点的坐标list
             clusterAssment[i,0]:第i个点输入哪个聚类
    """
    numSamples = dataSet.shape[0]
    # 首列是属于哪个类
    clusterAssment = mat(zeros((numSamples, 2)))
    clusterChanged = True

    # 初始化centroids
    centroids = initCentroids(dataSet, k)

    while clusterChanged:
        clusterChanged = False
        for i in range(numSamples):
            minDist = 1.0  # 最小距离
            minIndex = 0   # 最小距离对应的点群
            # 找到最近的centroid
            for j in range(k):
                distance = cosDistance(centroids[j, :], dataSet[i, :])  # 计算到数据的欧式距离
                if distance < minDist:  # 如果距离小于当前最小距离
                    minDist = distance  # 则最小距离更新
                    minIndex = j        # 对应的点群也会更新

            # 更新聚类
            if clusterAssment[i, 0] != minIndex:  # 如当前数据不属于该点群
                clusterChanged = True             # 聚类操作需要继续
                clusterAssment[i, :] = minIndex, minDist ** 2

        # 更新centroids
        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]  # 取列
            # nonzeros返回的是矩阵中非零的元素的[行号]和[列号]
            # .A是将mat对象转为array
            # 将所有等于当前点群j的，赋给pointsInCluster，之后计算该点群新的中心
            centroids[j, :] = mean(pointsInCluster, axis=0)  # 最后结果为两列，每一列为对应维的算术平方值

    print("Congratulations, cluster complete!")
    return centroids, clusterAssment
