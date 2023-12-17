
class Sender:

    def __init__(self) -> None:
        pass


    async def send_message(self, user, message, update):
        try:
            await update.message.reply_text(message)
        except Exception as e:
            print("Error in send_message: " + str(e))

    async def send_button_message(self, user, message, reply_markup, update):
        try:
            await update.message.reply_text(message, reply_markup=reply_markup)
        except Exception as e:
            print("Error in send_button_message: " + str(e))