
# coding: utf-8

# In[1]:

import PyPDF2
class convertCVtoText:
    @staticmethod
    def startConversion(fileName):
        pdfFileObj = open(fileName,'rb')     #'rb' for read binary mode
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        noOfPages=pdfReader.numPages
        text=""
        for pages in range(0,pdfReader.numPages):
            pageObj = pdfReader.getPage(pages)          #'9' is the page number
            text+=pageObj.extractText()
        return text


# In[ ]:



