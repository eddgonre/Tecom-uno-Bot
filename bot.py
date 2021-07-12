
# Dentro del import, el conversetionhandler es para hacer la conversacion
# MessageHandler para devolver un texto.
import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction

# Una variable para que el Bot se quede esperando el texto del QR
INPUT_TEXT = 0

def start(update, context):
    update.message.reply_text('Bienvenido a el Bot de Prueba, que desea hacer hoy?\n\n'
                              'Usa /qr para generar un codigo QR')
    # Despues de el start, le hace este comando, para el inicio del Bot

#aqui define una variable
def qr_command_handler(update,context):
    update.message.reply_text('Enviame un texto para hacer el codigo QR')
    return INPUT_TEXT

def generate_qr(text):
    filename = text + '.jpg'
    img = qrcode.make(text)
    img.save(filename)
    return filename

def send_qr(filename, chat):
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )

    chat.send_photo(
        photo=open(filename, 'rb')
    )

    os.unlink(filename)

def input_text(update, context):
    text = update.message.text
    print(text)
    #funcion que genera el codigo QR
    filename = generate_qr(text)
    chat = update.message.chat
    print(chat)
    print(filename)
    #funcion que envio el codigo QR el usuario.
    send_qr(filename, chat)

    return ConversationHandler.END
if __name__ == '__main__':

    # Aqui se defiene el Toiken que Genera el FatherBot, para el Bot
    # con un /revoque, puede hacer otro token.
    updater = Updater(token='1700677847:AAH3eCD1jA-QTDb4bmSGguRuwV1F0C9_Xi0', use_context=True)

    dp = updater.dispatcher

    # Con esto inicia el Bot, para que puede iniciar
    dp.add_handler(CommandHandler('start', start))

    #incia la concersacion con el la persona el Bot
    dp.add_handler(ConversationHandler(
        entry_points=[
                CommandHandler('qr',qr_command_handler)
        ],

        # Es en los momentos que el Bot esta esperando los estados de la coversacion
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]

        },

        fallbacks=[]

    ))

    updater.start_polling()
    updater.idle()

