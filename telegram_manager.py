#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import json
import time

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from user import UserManager, User
from controller import Controller
from experiences_manager import Experiences
from sender import Sender

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


ASK_NAME, ASK_AGE, ASK_GENDER, ASK_EMAIL, END = range(5)
user = User()

class Telegram:

    def __init__(self, user):
        self.user = user
        self.sender = Sender()


    # Comando /start
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

        user_info = update.effective_user
        user_message = update.message.text
        print(f"Received a message from {user_info.id}: {user_message}")
        self.user.id = user_info.id
        self.first_interaction = False

        buttons = [[KeyboardButton("Començar")]]
        await update.message.reply_text(
            "Benvingut al SexEd Bot, em dic Mara i estic aqui per ajudar-te!\n\n"
            "Pots cancelar en qualsevol moment escribint la comanda /cancel\n\n"
            "Ara començarem amb una serie de preguntes per conèixer-te millor",
            reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
        
        return ASK_NAME


    async def ask_name(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        message = "Com et dius?"
        await self.sender.send_message(user, message, update)
        
        return ASK_AGE


    async def ask_age(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.name = update.message.text

        message = "Quina és la teva edat?"
        await self.sender.send_message(user, message, update)
        
        return ASK_GENDER


    async def ask_gender(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.age = int(update.message.text)

        if self.user.age < 12:
            message = "Ho sentim, aquest assistent no pot ser utilitzat per menors de 12 anys"
            await self.sender.send_message(user, message, update)

            self.user.blocked = True
            UserManager().save_user(self.user)

            return ConversationHandler.END
        else:
            message = "Quin és el teu gènere?"
            await self.sender.send_message(user, message, update)
        return ASK_EMAIL


    async def ask_email(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

        self.user.gender = update.message.text
        message = "Quin és el teu email?"
        await self.sender.send_message(user, message, update)

        return END

    async def end(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        context.user_data['email'] = update.message.text  # Guardar el email
        self.user.first_interaction = False
        self.user.email = update.message.text
        UserManager().save_user(self.user)

        message = "Gràcies per completar l'onboarding 🎉"
        await self.sender.send_message(user, message, update)
        
        time.sleep(2)
        
        message = "Per qualsevol dubte, pots escriure en aquest mateix xat la paraula *Mara*, la teva assistent personal"
        await self.sender.send_message(user, message, update)

        time.sleep(2)
        
        message = "Prova a preguntar qualsevol cosa aqui mateix! 👇"
        await self.sender.send_message(user, message, update)

        return ConversationHandler.END


    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Cancels and ends the conversation."""
        user = update.message.from_user
        logger.info("User %s canceled the conversation.", user.first_name)
        await update.message.reply_text(
            "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
        )

        return ConversationHandler.END


    async def handle_mara(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user_input = update.message.text.lower()
        print("Here")

        if user_input == "mara":
            buttons = [
                [KeyboardButton("Questionari")],
                [KeyboardButton("Com funciona?")]
            ]
            message = "Hola, sóc la teva assistent virtual, Mara! 👋\n\n"
            message += "Pots preguntar-me qualsevol cosa sobre sexualitat i jo intentaré respondre't de la millor manera possible 🤓\n\n"
            message += "També pots fer click en els botons de sota per accedir a les diferents opcions que tinc per a tu! 👇"
            reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True)

            await self.sender.send_button_message(user, message, reply_markup, update)


    async def handle_query(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if self.user.status == "location":
            user_location = update.message.location
            user.location = {"la": user_location.latitude, "lo": user_location.longitude}
            response = Controller().nearest_center(self.user)
        else:
            user_info = update.effective_user
            user_message = update.message.text
            print(f"Received a message from {user_info.id}: {user_message}")
            response = Controller().handle_request(update.message.text, self.user.id)
        if response == "#ByronLove":
            await update.message.reply_text("Quina es la teva ubicació?")
            
        else:
            print(response)
            for res in response:
                await update.message.reply_text(res)


    async def handle_experience(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # We have to call ExperiencesManager to start the experience
        Experiences().handle_button(user, "exp_start")

def main() -> None:
    """Run bot."""
    user = User()
    telegram = Telegram(user)

    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6555434306:AAEMzna2BPLeoC7ggyauyWFIZFW4ut3FKXI").build()
    

    # Mara command handler
    mara_message_handler = MessageHandler(filters.Regex(r'(?i)\bmara\b'), telegram.handle_mara)
    application.add_handler(mara_message_handler)

    questionari_handler = MessageHandler(filters.Regex(r'(?i)\bquestionari\b'), telegram.handle_experience)
    application.add_handler(questionari_handler)

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO --> ONBOARDING
    onboarding_handler = ConversationHandler(
    entry_points=[CommandHandler("start", telegram.start)],
    states={
        ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, telegram.ask_name)],
        ASK_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, telegram.ask_age)],
        ASK_GENDER: [MessageHandler(filters.TEXT & ~filters.COMMAND, telegram.ask_gender)],
        ASK_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, telegram.ask_email)],
        END: [MessageHandler(filters.TEXT & ~filters.COMMAND, telegram.end)],
    },
    fallbacks=[CommandHandler("cancel", telegram.cancel)],)
    application.add_handler(onboarding_handler)

    # Handles conversation with AI
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, telegram.handle_query))
    

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    print("Starting server...")
    main()