from sklearn.preprocessing import normalize
from sklearn.feature_extraction.text import CountVectorizer
class NLTKHelper:
    def __init__(self):
        self.documentMatrix=None
        self.vocabulary=None
        self.normalizedFeatureSet=[]
    def findDocumentMatrix(self,totalCVText,minFrequency,vocab):
        #vectorizer=CountVectorizer(stop_words='english',min_df=minFrequency)
        vectorizer=CountVectorizer(stop_words='english',vocabulary=vocab)
        #vectorizer=CountVectorizer(stop_words='english')
        self.documentMatrix=vectorizer.fit_transform(totalCVText)
        self.vocabulary=vectorizer.vocabulary_
        #return documentMatrix,vocabulary 
        self.normalizeMatrix()
    def normalizeMatrix(self):
        self.normalizedFeatureSet=normalize(self.documentMatrix.toarray().astype('float64'))
        



