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
from user import UserManager
from controller import Controller

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

ASK_NAME, ASK_AGE, ASK_GENDER, ASK_EMAIL, END = range(5)



# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    buttons = [[KeyboardButton("Començar")]]
    await update.message.reply_text(
        "Benvingut al SexEd Bot, em dic Mara i estic aqui per ajudar-te!\n\n"
        "Pots cancelar en qualsevol moment escribint la comanda /cancel\n\n"
        "Ara començarem amb una serie de preguntes per conèixer-te millor",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    
    return ASK_NAME


async def ask_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Com et dius?")
    
    return ASK_AGE


async def ask_age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['name'] = update.message.text  # Guardar el nombre
    await update.message.reply_text("Quina és la teva edat?")
    
    return ASK_GENDER  # O el próximo estado si hay más pasos


async def ask_gender(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['age'] = update.message.text  # Guardar la edad
    await update.message.reply_text("Quin és el teu gènere?")
    
    return ASK_EMAIL


async def ask_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['gender'] = update.message.text  # Guardar el género
    await update.message.reply_text("Quin és el teu email?")

    return END

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['email'] = update.message.text  # Guardar el email
    await update.message.reply_text("Gràcies per completar l'onboarding.")

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


async def handle_mara(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text.lower()

    if user_input == "mara":
        buttons = [
            [KeyboardButton("Opción 1")],
            [KeyboardButton("Opción 2")]
        ]
        reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True)
        await update.message.reply_text("Panel de opciones para 'mara':", reply_markup=reply_markup)


async def handle_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Message: " + str(update.message.text))
    response = Controller().handle_request(update.message.text, "marcos")
    await update.message.reply_text(response)


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6555434306:AAEMzna2BPLeoC7ggyauyWFIZFW4ut3FKXI").build()
    
    print("Hey")
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_query))
    print("Heyyyyyy")

    # Si escribe "mara" en el chat, se ejecuta la función handle_mara
    mara_message_handler = MessageHandler(filters.Regex(r'(?i)\bmara\b'), handle_mara)
    application.add_handler(mara_message_handler)


    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    onboarding_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_name)],
        ASK_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_age)],
        ASK_GENDER: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_gender)],
        ASK_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_email)],
        END: [MessageHandler(filters.TEXT & ~filters.COMMAND, end)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
    )
    
    application.add_handler(onboarding_handler)


    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    print("Starting server...")
    main()