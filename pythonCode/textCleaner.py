import re
class textCleaner:
    def __init__(self):
        self.text=""
        self.cleanText=""
    def normalizeText(self):
        norText=""
        returnText=""
        norText+= re.sub(r'[^a-zA-Z ]',r' ',self.text)
        returnText+=re.sub(' +',' ',norText)
        self.cleanText+=re.sub(r'([A-Z])', lambda pat: pat.group(1).lower(), returnText)
       
                