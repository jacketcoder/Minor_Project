from tkinter import* 
from tkinter import StringVar, ttk
from communicationInformation import communicationInformation
from CVManager import CVManager
from tkinter import filedialog
from buttonHandler import buttonHandler 
class GUI:
    def __init__(self,root):
        self.passingInfo=communicationInformation()
        self.root=root
        self.run=False
        self.frame = Frame()
        self.frame.pack(fill=X)
        self.directoryLabel = Label(self.frame,text="Path",  width=10)
        self.directoryLabel.pack(side=LEFT)
        self.directoryEntry = Entry(self.frame,width=100)
        self.directoryEntry.pack(side=LEFT, padx=0,pady=10 ,expand=True)
        self.addDirectoryButton = Button(self.root, text ="     Add    ",command=self.pathAdd)
        self.addDirectoryButton.pack(padx=5,pady=10)
        self.buttonList=None
        self.jobReqFrame = Frame()
        self.jobReqFrame.pack(side=LEFT,fill=X)        
        self.jobRequirementLabel  = Label(self.jobReqFrame, text="Jobs Requirements", width=50)
        self.jobRequirementLabel.pack(expand=True, padx=5, pady=5)     
        self.relevantWordsText = Text(self.jobReqFrame,width=40,height=15)
        self.relevantWordsText.pack( side=LEFT,pady=5, padx=5)
        self.relevantWordsText.insert('1.0',' '.join(self.passingInfo.relevantWords))
        self.CVTitleFrame=Frame()
        self.CVTitleFrame.pack(fill=X)
        self.CVTitleLabel = Label(self.CVTitleFrame, text="Selecte Post", width=50)
        self.CVTitleLabel.pack( anchor=N, padx=0, pady=0)
        
        self.topCVDisplay = Frame()
        self.topCVDisplay.pack(fill=X,padx=50)
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.topCVDisplay, textvariable=self.box_value,state='readonly')
        self.box['values'] = ('game developer', 'animator', 'network engineer','web developer','DataScientist','Software developer')
        self.box.grid(column=0, row=0)
        
        #process button
        self.processButton = Button(self.jobReqFrame, text ="    Process    ",command=self.processExe)
        self.processButton.pack(side=LEFT,padx=10,pady=10)
        self.exitButton = Button(self.root, text ="    Exit    ",command=self.root.destroy)
        self.exitButton.pack(side=LEFT,padx=10,pady=10)
        self.manager=CVManager()

    def pathAdd(self):
        directoryPath=filedialog.askdirectory()
        self.directoryEntry.insert(0, directoryPath)
        
    def processExe(self):
        if(not(self.run)):
            self.passingInfo.directoryPath=self.directoryEntry.get()
            self.passingInfo.jobSelected=self.box.get()
            #self.passingInfo.relevantWords=self.relevantWordsText.get('1.0',END).strip().split(" ")
    #         if self.passingInfo.relevantWords:
    #             if self.passingInfo.jobSelected:
    #                 if self.passingInfo.directoryPath:
    #                     self.passingInfo.workFlow=True
            if self.passingInfo.workFlow:   
                try:
                    self.run=True
                    #print(self.passingInfo.relevantWords)
                    self.manager.list_CVs(self.passingInfo.directoryPath)
                    self.manager.collectCV()
                    self.manager.findDocumentMatrix(None,self.passingInfo.relevantWords)
                    self.manager.clusterData()
                    self.manager.rankCV()
                    self.manager.showAnalytics()
                    CVDataList=self.manager.showTopCVPerPost(self.passingInfo.jobSelected)
                    self.createLinkToCV(CVDataList)
                except Exception as e:
                    print("error")
                    print("processing \t"+str(e))
            else:
                print("select all necessary info")
        else:
            self.passingInfo.jobSelected=self.box.get()
            CVDataList=self.manager.showTopCVPerPost(self.passingInfo.jobSelected)
            self.buttonList.destoringButtons()
            self.createLinkToCV(CVDataList)
    def createLinkToCV(self,dataList):
        self.buttonList=buttonHandler(self.root,dataList)

   
