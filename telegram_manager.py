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
    CallbackContext,
    CallbackQueryHandler
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


ASK_NAME, ASK_AGE, ASK_SEX, ASK_EMAIL, END = range(5)
user = User()

class Telegram:

    def __init__(self, user):
        self.user = user
        self.sender = Sender()
        self.controller = Controller()


    # Comando /start
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        
        if self.user.first_interaction:
            user_info = update.effective_user
            user_message = update.message.text
            print(f"Received a message from {user_info.id}: {user_message}")
            self.user.id = user_info.id
            self.first_interaction = False

            buttons = [[KeyboardButton("Començar")]]
            await update.message.reply_text(
                "BENVINGUT al SexEd Bot, de BitsxLaMarató em dic Mara i estic aqui per ajudar-te!\n\n"
                "Pots cancelar en qualsevol moment escribint la comanda /cancel\n\n"
                "Ara començarem amb una serie de preguntes per conèixer-te millor",
                reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
            
            return ASK_NAME
        else:
            await self.sender.send_message(self.user, "Ja has completat l'onboarding! 👍", update)
            return ConversationHandler.END


    async def ask_name(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        message = "Com et dius? 🤔"
        await self.sender.send_message(user, message, update)
        
        return ASK_AGE


    async def ask_age(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.name = update.message.text

        message = "Quina és la teva edat? 📊"
        await self.sender.send_message(user, message, update)
        
        return ASK_SEX


    async def ask_sex(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.age = int(update.message.text)

        if self.user.age < 12:
            message = "Ho sentim, aquest assistent no pot ser utilitzat per menors de 12 anys 😔"
            await self.sender.send_message(user, message, update)

            self.user.blocked = True
            UserManager().save_user(self.user)

            return ConversationHandler.END
        else:
            message = "Quin és el teu sexe? 🤗"
            await self.sender.send_message(user, message, update)
        return ASK_EMAIL


    async def ask_email(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

        self.user.sex = update.message.text
        message = "Quin és el teu email? 📧"
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
            "Adéu! Gràcies per la teva visita!", reply_markup=ReplyKeyboardRemove()
        )

        return ConversationHandler.END


    async def handle_mara(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user_input = update.message.text.lower()
        print("Here")

        if user_input == "mara":
            buttons = [
                [KeyboardButton("Questionari")],
                [KeyboardButton("Com funciona?")],
                [KeyboardButton("Bibliografia")]
            ]
            message = "Hola, sóc Mara, la teva assistent virtual! 👋\n\n"
            message += "Pots preguntar-me qualsevol cosa sobre sexualitat i jo intentaré respondre't de la millor manera possible 🤓\n\n"
            message += "També pots fer click en els botons de sota per accedir a les diferents opcions que tinc per a tu! 👇"
            reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True)

            await self.sender.send_button_message(user, message, reply_markup, update)

        elif user_input == "questionari":
            self.user.experience_count += 1
            UserManager().save_user(self.user)
            await Experiences().handle_button(self.user, "exp_start", update)

        elif user_input == "com funciona?":
            message = "Hola! 👋 Sóc Mara, un assistent virtual expert en salut sexual i reproductiva. Tens algun dubte sobre temes com ITS, l’ús d’anticonceptius i la pornografia? Doncs a través d’aquest xat et podré ajudar a resoldre tots aquests problemes! 😊\n\nEscrivint /start podràs començar l’experiència i després d’una breu enquesta ja podràs conversar amb mi.\n\nSi en qualsevol moment vols revisar el menú principal, només cal que escriguis Mara 👍\n\nComencem? 😄"
            await self.sender.send_message(user, message, update)

        elif user_input == "bibliografia":
            message = "Sobre la salut sexual\n\nhttps://salutsexual.sidastudi.org/ca"
            await self.sender.send_message(user, message, update)
            time.sleep(5)
            message = "Com influeix la indústria del porno en la vida sexual de les noves generacions?\n\nhttps://www.ccma.cat/3cat/generacio-porno/"
            await self.sender.send_message(user, message, update)
            time.sleep(5)
            message = "Quin és el teu anticonceptiu ideal?\n\nhttps://decisionscompartides.gencat.cat/ca/decidir-sobre/anticoncepcio/quines_son_les_seves_preferencies/"
            await self.sender.send_message(user, message, update)


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
            await update.message.reply_text("Quina es la teva ubicació? 📍")
            
        else:
            print(response)
            for res in response:
                await update.message.reply_text(res)


    async def on_button_click(self, update: Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        data = query.data
        user = query.from_user

        experiences = json.load(open("questionari.json"))
        current_question = experiences[str(self.user.experience_count)]["question"]
        correct_answer = experiences[str(self.user.experience_count)]["correct"]

        if "correct" in data:
            response = "CORRECTE! ✅\n\nPregunta: " + current_question + "\nResposta: " + correct_answer
        else:
            response = "INCORRECTE! ❌\n\nPregunta: " + current_question + "\n\nResposta: " + correct_answer

        await query.edit_message_text(response)


    async def load_user(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        self.user = UserManager().load_user(self.user.id)
        message = "Id: " + str(self.user.id) + "\n"
        message += "Name: " + str(self.user.name) + "\n"
        message += "Sex: " + str(self.user.sex) + "\n"
        message += "Age: " + str(self.user.age) + "\n"
        message += "Email: " + str(self.user.email) + "\n"
        message += "Blocked: " + str(self.user.blocked) + "\n"
        message += "First Interaction: " + str(self.user.first_interaction) + "\n"
        message += "Experience Count: " + str(self.user.experience_count) + "\n"
        message += "Record: " + str(self.user.record)

        await self.sender.send_message(user, message, update)


        

def main() -> None:
    """Run bot."""
    user = User()
    telegram = Telegram(user)

    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6555434306:AAEMzna2BPLeoC7ggyauyWFIZFW4ut3FKXI").build()

    application.add_handler(CallbackQueryHandler(telegram.on_button_click))

    # Mara handler
    questionari_handler = MessageHandler(filters.Regex(r'(?i)\b(questionari|bibliografia|mara|com funciona?)\b'), telegram.handle_mara)
    application.add_handler(questionari_handler)

    # Onboarding Handler
    onboarding_handler = ConversationHandler(
    entry_points=[CommandHandler("start", telegram.start)],
    states={
        ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, telegram.ask_name)],
        ASK_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, telegram.ask_age)],
        ASK_SEX: [MessageHandler(filters.TEXT & ~filters.COMMAND, telegram.ask_sex)],
        ASK_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, telegram.ask_email)],
        END: [MessageHandler(filters.TEXT & ~filters.COMMAND, telegram.end)],
    },
    fallbacks=[CommandHandler("cancel", telegram.cancel)],)
    application.add_handler(onboarding_handler)

    # Handles conversation with AI
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, telegram.handle_query))

    # Dev commands
    user_command_handler = CommandHandler('user', telegram.load_user)
    application.add_handler(user_command_handler)

    # Experiences Handlers
    # exp_command_handler = CommandHandler('exp', telegram.handle_experience)
    # application.add_handler(exp_command_handler)
    

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    print("Starting server...")
    main()