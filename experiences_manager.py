import csv
import json

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton
from sender import Sender



class Experiences:

    def __init__(self):
        self.sender = Sender()

    def handle_button(self, user, content):
        if content == "exp_start":
            experiences = json.load(open("questionari.json"))

            experiences = json.load(open("questionari.json"))

            for i in range(20):
                print(experiences[str(i+1)])

                self.sender.send_message(user, experiences[str(i+1)]["question"], Update)


            print(experiences)