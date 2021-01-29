import os
class Attachment:
    
    def __init__(self):
        current_directory = os.getcwd()
        f = open(os.path.join(current_directory,"Final-Project\\attachment_list.txt"),"r")
        try:
            self.list_attachment = f.read().split('\n')
        except:
            self.list_attachment = []
        f.close()
        
    
    def get_attachments(self):
       return self.list_attachment