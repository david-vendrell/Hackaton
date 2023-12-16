
class User:
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.age = -1
        self.height = -1
        

class UserManager:

    def __init__(self):
        pass        
    
    def load_user(self, id):
        try:
            pass
        except Exception as e:
            print("Error in load_user: " + str(e))