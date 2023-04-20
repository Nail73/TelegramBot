import telebot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_WEATHER = InlineKeyboardButton('Погода', callback_data='weather')
BTN_WIND = InlineKeyboardButton('Ветер', callback_data='wind')
BTN_SUN_TIME = InlineKeyboardButton('Восход и закат', callback_data='sun_time')

BTN_CONVERT = InlineKeyboardButton('Курс биткоина', callback_data='currencies')
BTN_ANIMALS = InlineKeyboardButton('Фото', callback_data='animals')
BTN_POLL = InlineKeyboardButton('Опрос', callback_data='create_poll')

Samsung = InlineKeyboardButton('Samsung', callback_data='create_poll')
Iphone = InlineKeyboardButton('Iphone', callback_data='create_poll')


WEATHER = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND, BTN_SUN_TIME, BTN_CONVERT, BTN_ANIMALS, BTN_POLL)
WIND = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND, BTN_SUN_TIME, BTN_CONVERT, BTN_ANIMALS, BTN_POLL)
SUN_TIME = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND, BTN_SUN_TIME, BTN_CONVERT, BTN_ANIMALS, BTN_POLL)
HELP = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND, BTN_SUN_TIME, BTN_CONVERT, BTN_ANIMALS, BTN_POLL)

CONVERT = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND, BTN_SUN_TIME, BTN_CONVERT, BTN_ANIMALS, BTN_POLL)
ANIMALS = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND, BTN_SUN_TIME, BTN_CONVERT, BTN_ANIMALS, BTN_POLL)

POLL = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND, BTN_SUN_TIME, BTN_CONVERT, BTN_ANIMALS, BTN_POLL)