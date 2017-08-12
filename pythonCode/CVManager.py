from CV import CV
from NLTKHelper import NLTKHelper
from Clustering import Clustering
from CBRAlgo import CBRAlgo
import os
import matplotlib.pyplot as plt
import numpy as np
class CVManager:
    def __init__(self):
        self.CVList=[]
        self.cvsFile="documentMatrix.csv"
        self.CVFileName=[]
        self.fileNamesWithPath=[]
        self.cvPostList=[]
        self.CVTextColl=[]
        self.noOfTopCV=10
        self.orderedCVList=[]
        self.languageProcessing=None
        self.clusteringInfo=None
        self.CVRanker=None
    def list_CVs(self,rootPath):
          
        for root, dirs, files in os.walk(rootPath):
            for name in files:
                self.CVFileName.append(name)
                self.fileNamesWithPath.append(os.path.join(root, name))
                self.cvPostList.append(os.path.basename(os.path.dirname(os.path.join(root,name))))
               
    def collectCV(self):
            for cvFilePath,cvFileName,cvPost in zip(self.fileNamesWithPath,self.CVFileName,self.cvPostList):
                try:
                    newCV=CV(cvFileName,cvFilePath,cvPost)
                    self.CVList.append(newCV)
                except Exception as e:
                    print(cvFileName)
                    print("in collection of CV \t"+str(e))
            
    def collectCVText(self):
        self.CVTextColl=[]
        for cv in self.CVList:
            self.CVTextColl.append(cv.textHandeller.cleanText) 
    def findDocumentMatrix(self,minFrequency,vocab):
            self.collectCVText()
            self.languageProcessing=NLTKHelper()
            self.languageProcessing.findDocumentMatrix(self.CVTextColl,minFrequency,vocab)
            #df = pd.DataFrame(self.languageProcessing.documentMatrix.toarray())
            #df.to_csv(self.cvsFile)
            self.assignFeatureVector()  
    def assignFeatureVector(self):
#         for cv,cvNum in zip(self.CVList,range(0,len(self.CVFileName)-1)):
#             for featureRow in range(0,len(self.languageProcessing.vocabulary)-1):
#                 cv.featureVector.append(self.languageProcessing.normalizedFeatureSet[cvNum][featureRow])
        for cv,cvNum in zip(self.CVList,range(len(self.CVFileName))):
            cv.featureVector=self.languageProcessing.normalizedFeatureSet[cvNum]
        for cv,cvNum in zip(self.CVList,range(len(self.CVFileName))):
            cv.frequencyVector=self.languageProcessing.documentMatrix.toarray()[cvNum]
            #frequencyVector
    def makeGraph(self,data):
        lists = sorted(data) # sorted by key, return a list of tuples
        x, y = zip(*lists) # unpack a list of pairs into two tuples
        plt.plot(x, y)
        plt.show()
        
    def clusterData(self):
        self.clusteringInfo=Clustering()
        self.clusteringInfo.clusterData(self.languageProcessing.normalizedFeatureSet)
        self.makeGraph(self.clusteringInfo.silCoeffInfo.items())
    def rankCV(self):
        self.CVRanker=CBRAlgo()
        self.CVRanker.calculateCVScore(self.languageProcessing.documentMatrix,self.languageProcessing.vocabulary,self.clusteringInfo)
        for cv,cvScore in zip(self.CVList,self.CVRanker.CVScoreList):
            cv.score=cvScore
    def showAnalytics(self):
        self.CVRanker.plotTopWordsPerCluster()
        self.CVRanker.plotOverAllWeight(self.languageProcessing.vocabulary)
    def showTopCVPerPost(self,post):
        cvlist={}
        cvScore=[]
        cvData=[]
        if post is None:
            for cvCategery in set(self.cvPostList):
                cvlist={}
                print("cv of %s"%cvCategery)
                for cv in self.CVList:
                    if(cv.CVCategory==cvCategery):
                        cvlist.update({cv:cv.score})
                temp=[(value,key) for key,value in cvlist.items()]
                temp.sort()
                temp.reverse()
                temp=[(key,value) for value,key in temp]
                cvData=temp
                return cvData
        else:
            try:
                print("cv of post %s"%post)
                for cv in self.CVList:
                    if(cv.CVCategory==post):
                        cvlist.update({cv:cv.score})
                temp=[(value,key) for key,value in cvlist.items()]
                temp.sort()
                temp.reverse()
                temp=[(key,value) for value,key in temp]
                cvData=temp
                return cvData
            except Exception as e:
                    print(cv.fileName)
                    print("finding top CV \t"+str(e))
            
    def compareCV(self):
        topCVNum=2
        cvIndex=0
        #print(self.orderedCVList)
        for cvSample in self.orderedCVList[:topCVNum]:
            xValue = np.arange(len(cvSample[cvIndex].frequencyVector))
            plt.plot(xValue,cvSample[cvIndex].frequencyVector, markersize = 10,label=cvSample[cvIndex].fileName+'='+str(cvSample[cvIndex].score))
            #plt.rcParams["figure.figsize"] = (10,20)
        plt.title('CV comparision top cv')
        plt.ylabel('Feature Vector Frequency')
        plt.legend(mode="expand")
        plt.xlabel('Relevant words index')
        #plt.rcParams["figure.figsize"] = (10,10)
        plt.show()
        for cvSample in self.orderedCVList[int(len(self.orderedCVList)/2)-1:int(len(self.orderedCVList)/2)+1]:
            xValue = np.arange(len(cvSample[cvIndex].frequencyVector))
            plt.plot(xValue,cvSample[cvIndex].frequencyVector, markersize = 10,label=cvSample[cvIndex].fileName+'='+str(cvSample[cvIndex].score))
        plt.title('CV comparision middle CV')
        plt.ylabel('Feature Vector Frequency')
        plt.legend(mode="expand")
        plt.xlabel('Relevant words index')
        #plt.rcParams["figure.figsize"] = (10,10)
        plt.show()
        for cvSample in self.orderedCVList[-2:]:
            xValue = np.arange(len(cvSample[cvIndex].frequencyVector))
            plt.plot(xValue,cvSample[cvIndex].frequencyVector, markersize = 10,label=cvSample[cvIndex].fileName+'='+str(cvSample[cvIndex].score))
        plt.title('CV comparision last CV')
        plt.ylabel('Feature Vector Frequency')
        plt.legend(mode="expand")
        plt.xlabel('Relevant words index')
        #plt.rcParams["figure.figsize"] = (10,10)
        plt.show()
       
            
