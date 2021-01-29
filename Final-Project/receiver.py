import os
class Receiver:
    
    def __init__(self):
        current_directory = os.getcwd()
        f = open(os.path.join(current_directory,"Final-Project\\receiver_list.txt"),"r")
        try:
            self.list_receiver = f.read().split('\n')
        except:
            self.list_receiver = []
        f.close()
        
    
    def get_receiver(self):
       return self.list_receiver