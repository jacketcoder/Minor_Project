import webbrowser
from tkinter import*
class buttonHandler:
    def __init__(self, master,buttonDataList):
        self.buttonList=[]
        self.frame = Frame(master)
        self.frame.pack()
        for buttonName in buttonDataList:
                buttonToShow=Button(self.frame,text=str(buttonName[0][50:]),command=lambda:self.openPdf(buttonName[0]))
                buttonToShow.pack(padx=5,pady=10)
                self.buttonList.append(buttonToShow)
                
    def openPdf(self,link):
        webbrowser.open_new_tab(link) 
    def destoringButtons(self):
        self.frame.destroy()
        