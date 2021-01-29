import os
class Subject:
    
    def __init__(self):
        current_directory = os.getcwd()
        f = open(os.path.join(current_directory,"Final-Project\\subject.txt"),"r")
        try:
            #https://www.thecrazyprogrammer.com/2020/02/python-read-file-into-list.html
            self.list_subject = f.read().split('\n')
        except:
            self.list_subject = []
        f.close()
    
    def get_subject(self):
        if not(len(self.list_subject) == 0):
            return self.list_subject[0]
        else:
            return ""