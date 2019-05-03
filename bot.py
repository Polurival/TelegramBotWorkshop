import os
import random

import telebot
from telebot.types import Message
from telebot import apihelper

'''PROXY = {
    'http': 'socks5://telegram:telegram@qcpfo.tgproxy.me:3128',
    'https': 'socks5://telegram:telegram@qcpfo.tgproxy.me:1080'
}
apihelper.proxy = PROXY'''

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

smiles = [':+1:', ':kissing_closed_eyes:', ':joy:', ':kissing_heart:', ':heart:', ':heart_eyes:', ':blush:']


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello")


@bot.message_handler(func=lambda m: True)
def upper(message):
    bot.reply_to(message, random.choice(smiles))
    # bot.reply_to(message, message.text.upper())


bot.polling()
