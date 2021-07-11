from telegram.ext import Updater, CommandHandler

def start(update, context):

    update.message.reply_text('Hola Andrea')

if __name__ == '__main__':

    updater = Updater(token='1700677847:AAH3eCD1jA-QTDb4bmSGguRuwV1F0C9_Xi0', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

