#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from telegram import *
from telegram.ext import *
import telegram

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hola Soy El Bot La Hacker coloca /Help para ver mis comandos')





def info(update, context):
    """Send a message when the command /help is issued."""
    keyboard = [[InlineKeyboardButton("YouTube", url="https://www.youtube.com/opersweenlinux")],
                [InlineKeyboardButton("Grupo de Facebook", url="https://www.facebook.com/groups/kaliparanovatos")],
                [InlineKeyboardButton("Pagina de Facebook", url="https://www.facebook.com/kalilinuxparanovatos/")],
                [InlineKeyboardButton("Grupo telegram", url="https://t.me/kalilinuxparanovatosoficcial")],
                [InlineKeyboardButton("Canal Telegram", url="https://t.me/kalilinuxparanovatosoficial")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Hola soy La Hacker aqui te dejo la informacion: ",
                              reply_markup =reply_markup
                              )
def help(update, context):
    try:
        txt = open("funciones.txt", "r")
        responder = txt.read()
        txt.close()
        update.message.reply_text(responder)
    except:
        update.message.reply_text("Error en abrir el archivo")



def echo(update, context):
    """Echo the user message."""
    texto = update.message.text
    if texto.find("/"):
        update.message.reply_text(update.message.text)
    else:
        pass



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def reglas(update, context):
    #update.message.reply_text(" Pronto estaran las reglas")
    try:
        txt = open("reglas.txt", "r")
        responder = txt.read()
        txt.close()
        update.message.reply_text(responder)
    except:
        update.message.reply_text("Error en abrir el archivo")


def bot_conversacion(update, context):
    texto = update.message.text
    if texto.find("/"):
        chatbot = ChatBot('La Hacker')
        # Create a new trainer for the chatbot
        id = update.message.chat_id

        trainer = ChatterBotCorpusTrainer(chatbot)
        usuario = texto
        respuesta = chatbot.get_response(usuario)
        respuesta = str(respuesta)
        update.message.reply_text(respuesta)
        print("ID: " + str(id) + " Mensaje: " + usuario)
    else:
        pass


def charlar(update, context):
    update.message.reply_text("Hola quieres charlar conmigo, mandame privado y escribeme")
    id = update.message.chat_id
    print("ID: " +str(id))


def sumar(update, context):
    try:
        numero1 = int(context.args[0])
        numero2 = int(context.args[1])

        suma = numero1 + numero2

        update.message.reply_text("La suma es " +str(suma))
    except (ValueError):
        update.message.reply_text("Por favor coloque dos numeros")





def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher



    # on different commands - answer in Telegram

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("sumar", sumar))
    dp.add_handler(CommandHandler("reglas", reglas))
    dp.add_handler(CommandHandler("charlar", charlar))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    #dp.add_handler(MessageHandler(Filters.text, charla))

    dp.add_handler(MessageHandler(Filters.text, bot_conversacion))




    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()






#codigos de prueba

#def pizza(update, context):
#    if(update.message.text.upper().find("MANZANAS VERDES") > 0): #significa que existe la palabra
#        update.message.reply_text("Prefiero la pizza")

#def charla(update, context):
#    id = update.message.chat_id
#    mensaje = update.message.text
#    print("ID: " + str(id) + " Mensaje: " + mensaje)
#    try:
#        txt = open("charla.txt", "r")
#        responder = txt.read()
#        update.message.reply_text(responder)
#    except:
#        update.message.reply_text("Error en abrir el archivo")


