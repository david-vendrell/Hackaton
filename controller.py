from chatgpt import ChatGPT
from user import UserManager

class Controller:

    def __init__(self):
        pass


    def handle_request(self, content, id=None):
        try:
            if content:
                print("\n\n")
                print(content)
                user = UserManager().load_user(id)
                classification = ChatGPT().get_classification(user, content)
                print(classification)
                answer = ChatGPT().get_answer(user, content,str(classification["category"]))
                user.record.append({"role":"user", "content": content})
                user.record.append({"role":"assistant", "content": answer})
                return answer
                
        except Exception as e:
            print("Error handle_request: " + str(e))    
        

    