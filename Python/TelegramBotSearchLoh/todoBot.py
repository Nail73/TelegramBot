import telebot
import random
from telebot import types # для указание типов
import time

token = "5832710604:AAHXUDGvW3lBEAIE3Xa1TnOUF7PDXNzPuoE"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def init_button(message):

    start_button = "Узнать"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(start_button)

    bot.send_message(message.chat.id, 'Кто лох?'.format(message.from_user), reply_markup=markup)

@bot.message_handler(func=lambda message: message.text=='Узнать')
def send_message(message: types.Message):
    global i
    RANDOM_TASKS = ['Наиль', 'Олег', 'Андрей', 'Артём', 'Санёк', 'Виталя', 'Пётр', 'Илья', 'Коля', 'Говорят, каждый 3-й, поэтому вопрос открыт', 'Тчск, берега попутал, лохов искать?)',
    'Я конечно Бот и хорошо разбираюсь в лохах, но может стоит начать с себя? Не лох ли ты сам?)']

    word = ['Конечно же это - ',
    'А ты сомневался? Это - ',
    '100 пудов ты догадывался, что это - ',
    'Если он не в чате, не говорите, что лох - ',
    'Ну раз тебе так интересно, то вот он - ',
    'Для любопытных - ']

    stickers = ['CAACAgIAAxkBAAIZFWPI1X7Yj72NR4mzwossuti_LhgxAALlAQACFkJrCm6aK1JKYMuoLQQ',
    'CAACAgIAAxkBAAIZF2PI1Yr4YePy4FlJbjYkV2emjXeNAALoAQACFkJrCgtMrejShZ9SLQQ',
    'CAACAgIAAxkBAAIZGWPI1ZpaROaJlpixjQABFeSBAm-G-wAC9QEAAhZCawpH5OJk5K6gJi0E',
    'CAACAgIAAxkBAAIZG2PI1jNLUK6zy38P_GNweVUHwF8dAAJuFQACBTEhSLV4sVX9OW5TLQQ',
    'CAACAgIAAxkBAAIZHWPI1kZuOT0h_HyHRBYKVOcbJlAmAALWEwAC0c8YS1T_Fi-DniKrLQQ',
    'CAACAgIAAxkBAAIZH2PI1m5C0CVFiHI3xnnfVnWeCxzBAALmAQACFkJrCkbP8M3aTyDhLQQ',
    'CAACAgIAAxkBAAIZIWPI16AFrdys4y1xmcr6hf6mQ4sJAAKjEQACzeggS8P65ZndzIIQLQQ',
    'CAACAgIAAxkBAAIZI2PI1_y1QaLLOetuDjOXLvkr3_tVAAIRAAPANk8TDaqzD9wePuUtBA',
    'CAACAgIAAxkBAAIZJWPI2L6Vr252XR4OnZvFhyhJR4UkAAKgDQAC5O7pSjfRKZ3GFHqzLQQ',
    'CAACAgIAAxkBAAIZJ2PI2MZCJU4b-wSycFaN0tJGJo4VAAJoDAACyvNBSGjYfq69lG3FLQQ',
    'CAACAgIAAxkBAAIZKWPI2ONlo0Ybeoucfbc4g1B-T9ryAALzAANWnb0KahvrxMf6lv4tBA']

    now = ''
    message = bot.send_message(message.chat.id, f'*Поиск информации...* {now}', parse_mode="Markdown")
    text = random.choice(RANDOM_TASKS)
    time.sleep(1)
    message = bot.send_message(message.chat.id, f'*     Информация найдена...* {now}', parse_mode="Markdown")
    time.sleep(1)

    if text != 'Говорят, каждый 3-й, поэтому вопрос открыт' and text != 'Тчск, берега попутал, лохов искать?)'and text != 'Я конечно Бот и хорошо разбираюсь в лохах, но может стоит начать с себя? Не лох ли ты сам?)':

        bot.send_message(message.chat.id, random.choice(word) + text)
        time.sleep(2)
        bot.send_sticker(message.chat.id, random.choice(stickers))
        #message = bot.send_message(message.chat.id, f'*Соединение с ВК... изменение статуса ВК у лоха: * {text}', parse_mode="Markdown")

    else:
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
