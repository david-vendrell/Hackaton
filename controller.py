from telegram_manager import Telegram
from chatgpt import ChatGPT
class Controller:

    def __init__(self):
        pass


    def handle_request(self, type, content):
        try:
            if content:
                classification = ChatGPT().get_classification(content)
                answer = ChatGPT().get_classification(classification)
                
        except Exception as e:
            print("Error handle_request: " + str(e))    
        