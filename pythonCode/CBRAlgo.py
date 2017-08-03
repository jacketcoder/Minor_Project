from refiefFAlgo import refiefFAlgo 
import matplotlib.pyplot as plt
import matplotlib.pyplot as pl
import numpy as np
class CBRAlgo:
    def __init__(self):
        self.CVScoreList=[]
        self.topWords=None
        self.clusterWiseTopWordList=[]
        self.overAllWeight=[]
    def getTopWords(self,vocabulary,clusterCenters,noOfFormedClusters):
        x=[]
        for key,values in vocabulary.items():
            x.append(values)  
        self.topWords=refiefFAlgo()
        self.topWords.reliefF(clusterCenters,np.asarray(x),k=noOfFormedClusters-1)
        
    def getOverallWeightOfRelevantWords(self):
        self.overAllWeight=np.average([x for x in self.topWords.scoreList],axis=0)
        
    def calculateCVScoreViaCluster(self,documentMatrix,vocabulary,clusteringInfo):
        self.getTopWords(vocabulary,clusteringInfo.kMeans.cluster_centers_,clusteringInfo.bestClusterToForm)
        self.getTopWordsPerCluster(clusteringInfo.kMeans.cluster_centers_,vocabulary)
        self.getOverallWeightOfRelevantWords()
        featureVector=documentMatrix.toarray()
        for cvNumber,clusterNumber in enumerate(clusteringInfo.kMeans.labels_):
            score=0
            for wordFrequency,weight in zip(featureVector[cvNumber],self.topWords.scoreList[clusterNumber]):
                score+=wordFrequency*weight
            self.CVScoreList.append(score)    
            
    def calculateCVScore(self,documentMatrix,vocabulary,clusteringInfo):
        self.getTopWords(vocabulary,clusteringInfo.kMeans.cluster_centers_,clusteringInfo.bestClusterToForm)
        self.getTopWordsPerCluster(clusteringInfo.kMeans.cluster_centers_,vocabulary)
        self.getOverallWeightOfRelevantWords()
        featureVector=documentMatrix.toarray()
        for cvNumber,clusterNumber in enumerate(clusteringInfo.kMeans.labels_):
            score=0
            for wordFrequency,weight in zip(featureVector[cvNumber],self.overAllWeight):
                score+=wordFrequency*weight
            self.CVScoreList.append(score)    
            
    def getTopWordsPerCluster(self,clusterCenters,vocabulary):
        for clusterNo,impFeaturesRow in enumerate(clusterCenters):
            WordList={}
            for indexNo in self.topWords.wordIndex[clusterNo]:
                WordList.update({list(vocabulary.keys())[list(vocabulary.values()).index(indexNo)]:self.topWords.scoreList[clusterNo][indexNo]})
            self.clusterWiseTopWordList.append(WordList)
    def plotTopWordsPerCluster(self):
        topwords=10
        width =1
        for index,clusterTopWord in enumerate(self.clusterWiseTopWordList):
            ig,ax = plt.subplots()
            lists = [(key,value) for (key,value) in clusterTopWord.items()] # sorted by key, return a list of tuples
            key, value = zip(*lists)
            x = np.arange(topwords)
            plt.barh(x[:topwords],value[:topwords],align='center')
            plt.yticks(x, key[:topwords])
            #plt.rcParams["figure.figsize"] = (10,5)
            plt.title('top %d words in %d cluster'%(topwords,index))
            plt.ylabel('words')
            plt.xlabel('weight')
            plt.show()
    def plotOverAllWeight(self,vocabulary):
        ig,ax = plt.subplots()
        x = np.arange(0,len(self.overAllWeight))
        pl.barh(x,self.overAllWeight,align='center')
        pl.yticks(x,vocabulary)
        #pl.rcParams["figure.figsize"] = (1,1)
        pl.title('weight bar graph of Relevant words')
        pl.ylabel('words')
        pl.xlabel('weight')          
        pl.show()
