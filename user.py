import pickle
from redis_manager import RedisManager
class User:
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.age = -1
        self.height = -1
        
        #Record
        self.record = []
        

class UserManager:

    def __init__(self):
        pass
    
    def save_user(self, user):
        try:
            if not user:
                return

            pickle_obj = pickle.dumps(user)
            RedisManager().set(user.name, pickle_obj)
        except Exception as e:
            print("Error in save_user: " + str(e))
    
    def load_user(self, id):
        user = None
        value = RedisManager().get(id)
        user = pickle.loads(value)
        new_user = User()
        try:
            for attr in vars(user):
                try:
                    setattr(new_user, attr, vars(user)[attr])
                except Exception as e:
                    print(e)
                    pass
            return new_user
        except Exception as e:
            print("error in load user")
            print(e)
        return user 