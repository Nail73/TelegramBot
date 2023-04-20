from aiogram.contrib.middlewares import logging
import requests
from coordinates import get_coordinates
from api_service import get_weather
from weatherBot.bot import show_help_message


def weather() -> str:
    """Возвращает сообщение о температуре и описании погоды"""
    wthr = get_weather(get_coordinates())
    return f'{wthr.location}, {wthr.description}\n' \
           f'Температура: {wthr.temperature}°C, ощущается как {wthr.temperature_feeling}°C'


def wind() -> str:
    """Возвращает сообщение о направлении и скорости ветра"""
    wthr = get_weather(get_coordinates())
    return f'{wthr.wind_direction} wind {wthr.wind_speed} m/s'


def sun_time() -> str:
    """Возвращает сообщение о времени восхода и захода солнца"""
    wthr = get_weather(get_coordinates())
    return f'Восход: {wthr.sunrise.strftime("%H:%M")}\n' \
           f'Закат: {wthr.sunset.strftime("%H:%M")}\n'


def currencies() -> str:
    """Возвращает сообщение о курсе биткоина в долларах"""
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url).json()
    price = response['ticker']['last']
    curs = 'Курс биткоина к доллару составляет: ' + str(price) + ' usd'
    return curs


def animals() -> str:
    """Возвращает фото котиков"""
    URL = 'https://api.thecatapi.com/v1/images/search'
    DOGS_URL = 'https://api.thedogapi.com/v1/images/search'
    ERROR_MESSAGE = 'Ошибка при запросе к основному API: {error}'

    try:
        response = requests.get(URL)
    except Exception as error:
        logging.error(ERROR_MESSAGE.format(error=error))
        new_url = DOGS_URL
        response = requests.get(new_url)

    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def create_poll():
    return show_help_message
