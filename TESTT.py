from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, CallbackContext, Application

# Define stages
(NAME, EMAIL, CONFIRMATION) = range(3)

# Define callback data
(NAME_CALLBACK, EMAIL_CALLBACK, CONFIRM_CALLBACK) = ("name", "email", "confirm")


def start(update: Update, context: CallbackContext) -> int:
    keyboard = [[InlineKeyboardButton("Start Onboarding", callback_data=NAME_CALLBACK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to the Onboarding Bot. Click below to start.', reply_markup=reply_markup)
    return NAME

def name(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Please enter your name:")
    return EMAIL

def email(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user_name = query.message.text  # Save the name entered by the user
    context.user_data['name'] = user_name
    query.edit_message_text(text="Please enter your email:")
    return CONFIRMATION

def confirmation(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user_email = query.message.text  # Save the email entered by the user
    context.user_data['email'] = user_email
    keyboard = [[InlineKeyboardButton("Confirm", callback_data=CONFIRM_CALLBACK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Please confirm your details.", reply_markup=reply_markup)
    return -1  # End the conversation

def confirm(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    # Here, save or process user data
    name = context.user_data.get('name')
    email = context.user_data.get('email')
    query.edit_message_text(text=f"Thank you for completing the onboarding.\nName: {name}\nEmail: {email}")
    return ConversationHandler.END


def main():
    # Bot token
    TOKEN = "6555434306:AAEMzna2BPLeoC7ggyauyWFIZFW4ut3FKXI"

    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6555434306:AAEMzna2BPLeoC7ggyauyWFIZFW4ut3FKXI").build()

    # Define ConversationHandler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [CallbackQueryHandler(name, pattern=f'^{NAME_CALLBACK}$')],
            EMAIL: [CallbackQueryHandler(email, pattern=f'^{EMAIL_CALLBACK}$')],
            CONFIRMATION: [CallbackQueryHandler(confirmation, pattern=f'^{EMAIL_CALLBACK}$')]
        },
        fallbacks=[CommandHandler('start', start)]
    )


    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()




'''    buttons = [["Començar"]]
    await update.message.reply_text(
        "Benvingut al SexEd Bot, em dic Mara i estic aqui per ajudar-te!\n\n"
        "Pots cancelar en qualsevol moment escribint la comanda /cancel\n\n"
        "Ara començarem amb una serie de preguntes per conèixer-te millor", reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=False, input_field_placeholder="Prem el botó per començar!"))
    '''