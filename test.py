from telegram.ext import Updater, MessageHandler, Filters

def handle_message(update, context):
    chat_id = update.message.chat_id
    print("Chat ID:", chat_id)

def main():
    bot_token = '6490589708:AAERNMDkOlGbS6TXrlnKyGLUlWHwafIxozg'  # Reemplaza esto con tu token real de bot
    updater = Updater(token=bot_token, use_context=True)

    dispatcher = updater.dispatcher
    message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()  # Esto mantendrá al bot en ejecución hasta que lo detengas manualmente

if __name__ == '__main__':
    main()
