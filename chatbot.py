class chat_bot:
    def __init__(self):
        self.keywords=[]
        self.text=''
        self.word=''
        self.tolist()
    def get_response(self,User_text):
        self.text=User_text.lower().strip()
        for x in self.keywords:
            if self.isWordPresent(self.text,x):
                self.word=x
                break
        with open('training_data/more.txt','r') as file1:
            flag=0
            for line in file1:
                if line.strip()=='':
                    pass
                elif flag==2:
                    flag=0
                    return line 
                elif flag==0:
                    if line.lower().strip()==self.word:
                        flag=2
                elif flag==1:
                    flag=0

        return "Sorry I can't understand"


    def tolist(self):
        with open('training_data/more.txt','r') as file1:
            flag=0
            for line in file1:
                if line.strip()=='':
                    pass
                elif flag==0:
                    flag=1
                    word=line.strip()
                    self.keywords.append(word.lower())
                elif flag==1:
                    flag=0
        self.keywords.sort(key =len ,reverse=True)


    def isWordPresent(self,sentence, word):
        s = sentence.find(word)
        if s != -1:
            return True
        return False
