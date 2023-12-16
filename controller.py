from chatgpt import ChatGPT
from user import UserManager
class Controller:

    def __init__(self):
        pass


    def handle_request(self, content, id=None):
        try:
            if content:
                user = UserManager().load_user(id)
                classification = ChatGPT().get_classification(user, content)
                answer = ChatGPT().get_classification(user, classification, content)
                print(answer)
                
        except Exception as e:
            print("Error handle_request: " + str(e))    
        