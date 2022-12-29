import telebot
import random
from telebot import types # для указание типов
import time

import asyncio

token = " "

bot = telebot.TeleBot(token)

RANDOM_TASKS = ['Наиль', 'Олег', 'Андрей', 'Артём', 'Санёк', 'Виталя', 'Пётр', 'Илья', 'Коля']
task = random.choice(RANDOM_TASKS)

@bot.message_handler(commands=['start'])
def echo(message):

    start_button = "Узнать"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


    markup.add(start_button)

    bot.send_message(message.chat.id, "Кто в данный момент лох?".format(message.from_user), reply_markup=markup)

@bot.message_handler(func=lambda message: message.text=='Узнать')
def get_all(message: types.Message):

    cur_time = int(time.strftime("%M"))
    if cur_time >= 1 and cur_time <= 7:
        text = 'Наиль'
    elif cur_time >= 8 and cur_time <= 15:
        text = 'Олег'
    elif cur_time >= 16 and cur_time <= 23:
        text = 'Андрей'
    elif cur_time >= 24 and cur_time <= 31:
        text = 'Артём'
    elif cur_time >= 32 and cur_time <= 39:
        text = 'Санёк'
    elif cur_time >= 40 and cur_time <= 47:
        text = 'Виталя'
    elif cur_time >= 48 and cur_time <= 53:
        text = 'Пётр'
    elif cur_time >= 54 and cur_time <= 59:
        text = 'Илья'
    else:
        text = 'Коля'

    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
