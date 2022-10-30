from scipy import spatial
import pickle
import pandas as pd
import numpy as np

class Recommender():
    def __init__(self, paper_index):
        self.clusters = None
        self.XsT = None
        self.df = None
        self.get_clusters()

        self.paper_index = paper_index

        self.cluster = self.get_cluster()


    def get_clusters(self):
        with open('../pkl/clusers.pkl', 'rb') as file:
            self.clusters = pickle.load(file)
        with open('../pkl/XsT.pkl', 'rb') as file:
            self.XsT = pickle.load(file)
        self.df = pd.read_csv('../dataset/arxiv_sampled_processed.csv')

    def get_cluster(self):
        for i in range(len(self.clusters)):
            if self.paper_index in self.clusters[i]:
                return i
        return -1

    @staticmethod
    def get_cos_dis(point1, point2):
        return spatial.distance.cosine(point1, point2)

    def recommend_in_cluster(self):
        # recommend 3 papers in the same cluster
        res = []
        dis = []
        papers = self.clusters[self.cluster]

        for i, paper in enumerate(papers):
            if paper == self.paper_index:
                dis.append((paper, 10000))
            else:
                cos_dis = self.get_cos_dis(self.XsT[self.paper_index], self.XsT[paper])
                dis.append((paper, cos_dis))

        dis.sort(key = lambda x : x[1])
        top3 = dis[:3]
        for t in top3:
            res.append((t[0], self.df.loc[t[0], 'title'].replace('\n', '')))

        return res

    def recommend_out_cluster(self):
        # recommend 2 papers in different cluster
        res = []
        dis = []
        papers = self.clusters[self.cluster]
        for i in range(self.df.shape[0]):
            if i in papers:
                continue
            else:
                cos_dis = self.get_cos_dis(self.XsT[self.paper_index], self.XsT[i])
                dis.append((i, cos_dis))

        dis.sort(key=lambda x: x[1])
        top2 = dis[:2]
        for t in top2:
            res.append((t[0], self.df.loc[t[0], 'title'].replace('\n', '')))

        return res

    def recommend(self):
        in_cluster = self.recommend_in_cluster()
        out_cluster = self.recommend_out_cluster()

        return [in_cluster, out_cluster]

