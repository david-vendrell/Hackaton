import requests
from user import UserManager
from bs4 import BeautifulSoup  #del módulo bs4, necesitamos BeautifulSoup

import schedule

API_TOKEN = "6555434306:AAEMzna2BPLeoC7ggyauyWFIZFW4ut3FKXI"

class Telegram:
    
    def __init__(self):
        pass


    def send_telegram_message(self, bot_token, chat_id, message):
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(url, data=data)
        return response.json()


    #send_telegram_message(bot_token, chat_id, message)


    


message = 'Hello, this is a test message from my bot.'

#Telegram().send_telegram_message(bot_token, chat_id, message)






def bot_send_text(bot_message):
    
    bot_token = "6490589708:AAERNMDkOlGbS6TXrlnKyGLUlWHwafIxozg"
    chat_id = '988592334'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response


bot_send_text('Hello World!')