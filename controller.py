from chatgpt import ChatGPT
from user import UserManager
from telegram_manager import main
from user import UserManager, User

class Controller:

    def __init__(self):
        pass


    def handle_request(self, content, id=None):
        try:
            if content:
                user = UserManager().load_user(id)
                print(user.name)
                classification = ChatGPT().get_classification(user, content)
                answer = ChatGPT().get_answer(user, content,str(classification["category"]))
                return answer
                
        except Exception as e:
            print("Error handle_request: " + str(e))    
        
    