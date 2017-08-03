from textCleaner import textCleaner
from convertCVtoText import convertCVtoText
class CV:
     def __init__(self,name,path,post):
            self.fileName=name
            self.filePath=path
            self.CVCategory=post
            self.textHandeller=textCleaner()
            self.textHandeller.text=convertCVtoText.startConversion(self.filePath)
            self.textHandeller.normalizeText()
            self.featureVector=[]
            self.score=None



