import webbrowser
from tkinter import*
import random
class buttonHandler:
    def __init__(self, master,buttonDataList):
        self.buttonList=[]
        self.frame = Frame(master)
        self.frame.pack()
        vhdlWork=[]
        f=open("F:\\VHDL\\text.txt","w")
        for buttonName in buttonDataList:
                buttonToShow=Button(self.frame,text=str(buttonName[0].fileName),command=lambda:self.openPdf(buttonName[0].filePath))
                #f.write(
                value=str(str(buttonName[0].fileName[:10])+" "+str(int(buttonName[1]))+"\n")
                vhdlWork.append(value)
                buttonToShow.pack(padx=5,pady=10)
                self.buttonList.append(buttonToShow)
        random.shuffle(vhdlWork)
        for eachLine in vhdlWork:
            f.write(eachLine)
        f.close()
    def openPdf(self,link):
        webbrowser.open_new_tab(link) 
    def destoringButtons(self):
        self.frame.destroy()
        
    