class communicationInformation:
    def __init__(self):
        self.directoryPath=""
        #self.relevantWords=[]
        self.jobSelected=""
        self.workFlow=True
        relevantWords1=[
'ip',
   'firewall',
'layer',
     'wan',
   'protocol',
     'router',
     'switch',
     'traffic',
      'css',
   'design',
  'html',
  'javascript',
 'jquery',
 'mysql',
  'ajax',
     'php',
   'unity','game','team','computer','engine','software','programming','developer','microsoft','project',
    'animation','adobe','flash','character','art','illustrator','design','animator','effects','maya','photoshop',
    
   "software","skills","application","developer","server",
   "systems","framework","net","visual",
    
     "algorithm","analyst","aws","datasets","clustering","intelligence","logistic","mining","neural","regression","scikit"

    

]
        self.relevantWords=list(set(relevantWords1))