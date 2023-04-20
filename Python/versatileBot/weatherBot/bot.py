import logging

from aiogram import Bot, Dispatcher, executor, types
import config
import inline_keyboard
import messages

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['weather', 'Погода'])
async def show_weather(message: types.Message):
    await message.answer(text=messages.weather(),
                         reply_markup=inline_keyboard.WEATHER)


@dp.message_handler(commands='start')
async def show_help_message(message: types.Message):
    await message.answer(
        text=f'*Привет, {message.from_user.first_name}! Я многофункциональный бот и умею выполнять разные задачи. Ниже кнопки на выбор.*',
        parse_mode='Markdown',
        reply_markup=inline_keyboard.HELP)


@dp.message_handler(commands='wind')
async def show_wind(message: types.Message):
    await message.answer(text=messages.wind(), reply_markup=inline_keyboard.WIND)


@dp.message_handler(commands='sun_time')
async def show_sun_time(message: types.Message):
    await message.answer(text=messages.sun_time(), reply_markup=inline_keyboard.SUN_TIME)


@dp.message_handler(commands='currencies')
async def show_currencies(message: types.Message):
    await message.answer(text=messages.currencies(), reply_markup=inline_keyboard.CONVERT)


@dp.message_handler(commands='animals')
async def show_animals(message: types.Message):
    await message.answer(text=messages.animals(), reply_markup=inline_keyboard.ANIMALS)


@dp.message_handler(commands='create_poll')
async def show_start_create_poll(message: types.Message):
    await message.answer(text=messages.create_poll(), reply_markup=inline_keyboard.POLL)


@dp.callback_query_handler(text='weather')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.weather(),
        reply_markup=inline_keyboard.WEATHER
    )


@dp.callback_query_handler(text='wind')
async def process_callback_wind(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.wind(),
        reply_markup=inline_keyboard.WIND
    )


@dp.callback_query_handler(text='sun_time')
async def process_callback_sun_time(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.sun_time(),
        reply_markup=inline_keyboard.SUN_TIME
    )


@dp.callback_query_handler(text='currencies')
async def process_callback_currencies(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.currencies(),
        reply_markup=inline_keyboard.CONVERT
    )


@dp.callback_query_handler(text='animals')
async def process_callback_animals(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.animals(),
        reply_markup=inline_keyboard.ANIMALS
    )


@dp.callback_query_handler(text='create_poll')
async def process_callback_create_poll(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        "Какой телефон лучше?",
        reply_markup=inline_keyboard.POLL
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
