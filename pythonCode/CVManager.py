from CV import CV
from NLTKHelper import NLTKHelper
from Clustering import Clustering
from CBRAlgo import CBRAlgo
import os
import matplotlib.pyplot as plt
class CVManager:
    def __init__(self):
        self.CVList=[]
        self.cvsFile="documentMatrix.csv"
        self.CVFileName=[]
        self.fileNamesWithPath=[]
        self.cvPostList=[]
        self.CVTextColl=[]
        self.noOfTopCV=10
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
        for cv,cvNum in zip(self.CVList,range(0,len(self.CVFileName)-1)):
            for featureRow in range(0,len(self.languageProcessing.vocabulary)-1):
                cv.featureVector.append(self.languageProcessing.normalizedFeatureSet[cvNum][featureRow])
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
                        cvlist.update({cv.fileName:cv.score})
                temp=[(value,key) for key,value in cvlist.items()]
                temp.sort()
                temp.reverse()
                temp=[(key,value) for value,key in temp]
                cvData=temp
                return cvData[:self.noOfTopCV]
        else:
            print("cv of post %s"%post)
            for cv in self.CVList:
                if(cv.CVCategory==post):
                    cvlist.update({cv.filePath:cv.score})
            temp=[(value,key) for key,value in cvlist.items()]
            temp.sort()
            temp.reverse()
            temp=[(key,value) for value,key in temp]
            cvData=temp
            return cvData[:self.noOfTopCV]
            
            
