import jieba
import json
from cos_kmeans import *
from numpy import *


class routes_cluster:
    """
    1. 读入每个城市数据，获取每条线路的行程 list
    2. 将每个 list 中的字符串使用结巴分词，得到分词信息
    3. 将分词结果与景点名匹配，将匹配到的景点名组合成一个线路 list，将涉及到的景点名组合成另一个总景点名 list
    4. 将每条线路的景点名 list 按照总景点名 list，映射成向量
    5. 使用重写的 cos_kmeans 聚类（将 kmeans 中的欧氏距离换成余弦相似度，以用于文本聚类）
    6. 将每一类的中心坐标反向映射为景点名
    7. 将3中每条线路的景点名 list 与 6 中的景点名 list 匹配，匹配度高的为一类
    """

    def __init__(self, city):
        """
        读入指定城市的旅游线路数据
        """
        # 城市名
        self.city = city

        # 每条线路信息list，里面存dict：编号、线路名、行程
        self.routes_info = []

        # 所有线路行程list
        self.plans = []

        # 读取json文件
        with open('../spider/routes/routes_data/formatted_data/' + city + '.json', 'r', encoding='utf8') as fp:
            json_data = json.load(fp)
        for route in json_data:
            self.plans.append(route['行程'])
            self.routes_info.append({'url': route['url'], 'route_name': route['线路名'], 'scene': []})

        # 读取json文件
        with open('../spider/scene/name/' + city + '.json', 'r', encoding='utf8') as fp_scene:
            # 所有景点名
            self.all_scenes = json.load(fp_scene)
        # 该城市所有线路涉及到的总景点名list
        self.all_scenes_of_city = []

        # 可以用来聚类的dataset: 每条线路景点映射成向量后拼成的矩阵
        self.all_routes_vec = []

    def get_scenes_of_routes(self):
        """
        将每个list中的字符串使用结巴分词，得到分词信息,并与景点名匹配，
        将匹配到的景点用编号替代，每条线路重新得到一个数字list
        """
        i = 0
        # 遍历每个行程
        for route in self.plans:
            plan = ''

            # 遍历每天行程
            for day in route:
                # 组合成一个字符串
                plan = plan + day

            # 去除全部空格
            plan = plan.replace(" ", "")
            # 分词，返回list
            plan_seg_list = jieba.lcut(plan, cut_all=True)

            # 遍历，匹配分词后的list和景点名
            # 每条线路匹配到的景点名list
            scene_of_route = []
            for word in plan_seg_list:
                for scene in self.all_scenes:
                    if word in scene:
                        if scene in scene_of_route:
                            break
                        else:
                            scene_of_route.append(scene)
                            if scene in self.all_scenes_of_city:
                                break
                            else:
                                self.all_scenes_of_city.append(scene)
                                break

            self.routes_info[i]['scene'] = scene_of_route
            i = i + 1

        for k in range(0, len(self.routes_info)):  # 对第k条线路
            # 初始化向量
            vec = [0] * (len(self.all_scenes_of_city))

            # 遍历所有景点匹配向量值
            if len(self.routes_info[k]['scene']) != 0:
                for x in range(0, len(self.all_scenes_of_city)):  # 对所有景点中的每一个
                    for y in range(0, len(self.routes_info[k]['scene'])):  # 对第k条线路中的每个景点
                        if self.routes_info[k]['scene'][y] == self.all_scenes_of_city[x]:
                            # print(self.all_scenes_of_city[x])
                            vec[x] = 1
            print(vec)
            n = 0
            for z in range(0, len(vec)):
                if vec[z] == 1:
                    n = n + 1
            print(n)
            self.all_routes_vec.append(vec)

    def get_centroids_scenes(self, centroids):
        """
        得到聚类中心对应的景点
        :param centroids: 聚类中心点向量
        :return:聚类中心对应的景点
        """

        # 聚类中心点向量list
        centers = []
        # 聚类中心点对应景点list
        centroids_scenes = []

        for cen in centroids:
            num = 0
            for i in range(len(cen)):
                if cen[i] > 0.8:
                    num = num + 1
            print(num)
            if num < 7 and num > 1:
                centers.append(cen)

        for cen in centers:
            # 得到聚类中心对应的景点(反向映射)
            cen_scenes = []
            for i in range(len(cen)):
                if cen[i] > 0.8:
                    cen_scenes.append(self.all_scenes_of_city[i])

            centroids_scenes.append(cen_scenes)

        return centroids_scenes

    def routes_in_clusters(self, centroids_scenes):
        """

        :param centroids_scenes:
        :return:
        """
        # 创建存放最终结果的list
        out = []

        # 遍历每个聚类，得到每个类的线路
        for center in centroids_scenes:
            tourist_route = []
            cluster_name = ''
            for s in center:
                cluster_name = cluster_name + s + ' + '
            cluster_name = cluster_name[:-3]

            for k in range(0, len(self.routes_info)): # 对第k条线路
                num = 0
                for i in range(0, len(self.routes_info[k]['scene'])): # 对第k条线路中的第i个景点
                    if self.routes_info[k]['scene'][i] in center:
                        num = num + 1
                if num > 2:
                    tourist_route.append({'route_name': self.routes_info[k]['route_name'], 'url': self.routes_info[k]['url']})

            # 整理最终的数据格式
            if len(tourist_route) != 0:
                cluster_dict = {'cluster_name': cluster_name, 'tourist_route': tourist_route}
                out.append(cluster_dict)

        return out

    def run(self):
        """
        总控函数
        """
        # 得到每个线路的景点信息
        self.get_scenes_of_routes()
        # 转换成可以聚类的格式
        dataSet = array(self.all_routes_vec)

        # 设定聚类个数
        k = 6
        # 进行聚类
        centroids, clusterAssment = kmeans(dataSet, k)

        # 得到聚类中心对应的景点
        centroids_scenes = self.get_centroids_scenes(centroids)
        # 得到每一类的具体线路
        out = self.routes_in_clusters(centroids_scenes)

        data = json.dumps(out, indent=4, ensure_ascii=False)
        with open('result/' + self.city + '.json', 'w', encoding='utf8') as f:
            data = str(data)
            f.write(data)
            f.close()


if __name__ == '__main__':
    '''
    每个城市线路的数据预处理
    '''
    # 以上海为例，可更换城市名
    city = routes_cluster('上海')
    city.run()
