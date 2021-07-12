from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

INPUT_TEXT = 0

def start(update, context):

    But_PaginaWeb = InlineKeyboardButton(
        text='Tecom Sistemas'
        url='http://www.tecomcr.com'
    )

    update.message.reply_text(
        text='Los botones'
    )

if __name__ == '__main__':
    updater = Updater(token='1700677847:AAH3eCD1jA-QTDb4bmSGguRuwV1F0C9_Xi0', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()
