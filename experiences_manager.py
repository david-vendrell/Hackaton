import csv
import json

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from sender import Sender


class Experiences:

    def __init__(self):
        self.sender = Sender()

    async def handle_button(self, user, content, update):
        if content == "exp_start":
            experiences = json.load(open("questionari.json"))
            print(experiences)

            current_question = experiences[str(user.experience_count)]["question"]
            print(current_question)
            correct_answer = experiences[str(user.experience_count)]["correct"]
            print(correct_answer)

            buttons = []
            for i in range(1, 5):
                print(i)
                it = "answer" + str(i)
                answer = experiences[str(user.experience_count)][it]
                print(answer)
                callback_data = f"exp_answer{i}_{'correct' if answer == correct_answer else 'wrong'}"
                buttons.append([InlineKeyboardButton(answer, callback_data=callback_data)])
                reply_markup = InlineKeyboardMarkup(buttons)


            await self.sender.send_button_message(user, experiences[str(user.experience_count)]["question"], reply_markup, update)

