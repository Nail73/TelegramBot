import asyncio
import datetime
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from config import token, user_id
from main import check_comp_update

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Все товары", "Последние 5 товаров", "Свежие товары"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Список товаров", reply_markup=keyboard)


@dp.message_handler(Text(equals="Все товары"))
async def get_all_comp(message: types.Message):
    with open("comp_dict.json") as file:
        comp_dict = json.load(file)

    for k, v in sorted(comp_dict.items()):
        comp = f"{hlink(v['article_url'], v['article_title'])}"

        await message.answer(comp)


@dp.message_handler(Text(equals="Последние 5 товаров"))
async def get_last_five_comp(message: types.Message):
    with open("comp_dict.json") as file:
        comp_dict = json.load(file)

    for k, v in sorted(comp_dict.items())[-5:]:
        comp = f"{hlink(v['article_url'], v['article_title'])}"

        await message.answer(comp)


@dp.message_handler(Text(equals="Свежие товары"))
async def get_fresh_comp(message: types.Message):
    fresh_comp = check_comp_update()

    if len(fresh_comp) >= 1:
        for k, v in sorted(fresh_comp.items()):
            comp = f"{hlink(v['article_url'], v['article_title'])}"

            await message.answer(comp)

    else:
        await message.answer("Пока нет новых товаров...")


async def comp_every_minute():
    while True:
        fresh_comp = check_comp_update()

        if len(fresh_comp) >= 1:
            for k, v in sorted(fresh_comp.items()):
                comp = f"{hlink(v['article_url'], v['article_title'])}"

                # get your id @userinfobot
                await bot.send_message(user_id, comp, disable_notification=True)

        # else:
        #     await bot.send_message(user_id, "Пока нет новых товаров...", disable_notification=True)

        await asyncio.sleep(10)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(comp_every_minute())
    executor.start_polling(dp)
