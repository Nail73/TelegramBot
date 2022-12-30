import telebot
import random
from telebot import types # для указание типов
import time

token = "5832710604:AAHXUDGvW3lBEAIE3Xa1TnOUF7PDXNzPuoE"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def echo(message):

    start_button = "Узнать"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(start_button)

    bot.send_message(message.chat.id, "Кто в данный момент лох?".format(message.from_user), reply_markup=markup)

@bot.message_handler(func=lambda message: message.text=='Узнать')
def get_all(message: types.Message):

    RANDOM_TASKS = ['Наиль', 'Олег', 'Андрей', 'Артём', 'Санёк', 'Виталя', 'Пётр', 'Илья', 'Коля', 'Говорят, каждый 3-й, поэтому вопрос открыт', 'Тчск, берега попутал, лохов искать?)']
    url = ['https://www.factroom.ru/wp-content/uploads/2022/01/3-18.jpg',
    'https://www.factroom.ru/wp-content/uploads/2022/01/1-21.jpg',
    'https://www.factroom.ru/wp-content/uploads/2022/01/7-10.jpg',
    'https://www.factroom.ru/wp-content/uploads/2022/01/5-11.jpg',
    'https://www.factroom.ru/wp-content/uploads/2022/01/4-11.jpg',
    'https://www.factroom.ru/wp-content/uploads/2022/01/1-19.jpg',
    'https://www.factroom.ru/wp-content/uploads/2022/01/8-9.jpg',
    'https://www.factroom.ru/wp-content/uploads/2022/01/6-10.jpg']

    word = ['Конечно же это - ',
    'А ты сомневался? Это - ',
    '100 пудов ты догадывался, что это - ',
    'Если он не в чате, не говорите, что лох - ',
    'Ну раз тебе так интересно, то вот он - ',
    'Для люопытных - ']
    text = random.choice(RANDOM_TASKS)

    if text != 'Говорят, каждый 3-й, поэтому вопрос открыт' and text != 'Тчск, берега попутал, лохов искать?)':
        bot.send_message(message.chat.id, random.choice(word) + text)
        bot.send_message(message.chat.id, 'Интересный факт, чтобы не быть лохом: ')
        bot.send_message(message.chat.id, random.choice(url))
    else:
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
