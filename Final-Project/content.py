import os
class Content:
    
    def __init__(self):
        current_directory = os.getcwd()
        f = open(os.path.join(current_directory,"Final-Project\\content_email.txt"),"r")
        try:
            #https://www.thecrazyprogrammer.com/2020/02/python-read-file-into-list.html
            self.content = f.read()
        except:
            self.content
        f.close()
    
    def get_content(self):
        return self.content