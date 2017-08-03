
# coding: utf-8

# In[1]:

from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
class Clustering:
    def __init__(self):
        self.kMeans=None
        self.bestClusterToForm=None
        self.silCoeffInfo={}
        self.minCluster=2
        self.maxCluster=10
    def findSilCoeff(self,data):
        for n_cluster in range(self.minCluster, self.maxCluster):
            kmeans = KMeans(n_clusters=n_cluster).fit(data)
            label = kmeans.labels_
            sil_coeff = silhouette_score(data, label, metric='euclidean')
            self.silCoeffInfo.update({n_cluster:float(sil_coeff)})
        maxSilCoeff=max(self.silCoeffInfo.values())
        maxSilCoeffkeys = [k for k, v in self.silCoeffInfo.items() if v == maxSilCoeff]
        if(len(maxSilCoeffkeys)==1):
            for x in maxSilCoeffkeys:
                self.bestClusterToForm=x
        else:
            print("2 keys,confusion")
    def clusterData(self,data):
        self.findSilCoeff(data)
        self.kMeans=KMeans(n_clusters=self.bestClusterToForm).fit(data)


