from sqlite3 import IntegrityError
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from weather import *
from Keyboards import kb_client
from Keyboards import kb_client_clear
from data_base import database
from datetime import timedelta, datetime

import os

async def on_startup(_):
    print("Bot start")
    database.sql_start()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)
all_cities = {
                "/Київ": "Kyiv",
                "/Харків": "Kharkiv",
                "/Одеса": "Odesa",
                "/Дніпро": "Dnipropetrovsk",
                "/Донецьк": "Donetsk",
                "/Запоріжжя": "Zaporizhzhia",
                "/Львів": "Lviv",
                "/Кривий_Ріг": "Krivyirih",
                "/Миколаїв": "Mikolaiv",
                "/Маріуполь": "Mariupol",
                "/Луганськ": "Luhansk",
                "/Вінниця": "Vinnitsa",
                "/Херсон": "Kherson",
                "/Чернігів": "Chernigiv",
                "/Полтава": "Poltava",
                "/Черкаси": "Chercasy",
                "/Хмельницький": "Khmelnytskyi",
                "/Чернівці": "Chernivtsi",
                "/Житомир": "Zhytomyr",
                "/Тернопіль": "Ternopil",
                "/Рівне": "Rovenska",
                "/Крим": "Crimea",
                "/Суми": "Sumy"
              }

async def weather_detal_output(message: types.Message, time, weather_detal_day):
    city = await database.user_check(message.from_user.id)
    stra = ""
    if (city != None):
        stra = "Погода в місті "+ city[0] + " за "+ time +"\n"
        weather = weather_detal(weather_detal_day, city[0])
        for key, (value, value1) in weather.items():
            stra = stra + key + "    " + value + "   " + value1 + "\n"
    else:
        stra = "Введіть Місто через /\n"
        for key, value in all_cities.items():
            stra = stra + "  " + key +"\n"
    await message.answer(stra)

@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Привіт, виберіть область, яка вас цікавить ", reply_markup=kb_client)
    except:
        await message.reply("Напишите пожалуйста боту в личку \n @ssspammmbot")
    print(message.from_user.id)

@dp.message_handler(commands=["погода_сьогодні"])
async def weather1(message: types.Message):
    await weather_detal_output(message, str(datetime.now()), 0)

@dp.message_handler(commands=["погода_завтра"])
async def weather2(message: types.Message):
    await weather_detal_output(message, str(datetime.now() + timedelta(days=1)), 1)

@dp.message_handler(commands=["погода_після_завтра"])
async def weather3(message: types.Message):
    await weather_detal_output(message, str(datetime.now() + timedelta(days=2)), 2)

@dp.message_handler(commands=["погода_через_2_дні"])
async def weather4(message: types.Message):
    await weather_detal_output(message, str(datetime.now() + timedelta(days=3)), 3)

@dp.message_handler(commands=["all_cities"])
async def help_all_cities(message: types.Message):
    stra = "Введіть Місто через /\n"
    for key, value in all_cities.items():
        stra = stra + "  " + key + "\n"
    await message.reply(stra)

@dp.message_handler(commands=["dead_orcs"])
async def dead_orcs(message: types.Message):
    await message.reply(dead_rusnia("06"))

@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.reply("Для того, щоб вибрати місто яке вас цікавить введіть /all_cities")

@dp.message_handler()
async def message_all(message: types.Message):
    if all_cities.get(message.text):
        try:
            await database.new_user_db(message.from_user.id, all_cities.get(message.text))
        except IntegrityError:
            await database.user_update(message.from_user.id, all_cities.get(message.text))

    if message.text == "/capybara":
        img = open('images/hellinheavns-capybara.gif', 'rb')
        await bot.send_video(message.from_user.id, img, None, 'Text')
        img.close()

    if message.text == "/hide_keyboard":
        await bot.send_message(message.chat.id, "Убрать клавиатуру", reply_markup=kb_client_clear)


#-------------------------CLIENT-------------------------------------


# async def weather_shorty(message: types.Message):
#     arr1 = weather_short()
#     if message.text == "Погода_Р":
#         stra = "🌑   Ніч  " + arr1[0] + "\n" + "☀   Ранок  " + arr1[1] + "\n" + "🌤   День   " + arr1[2] + "\n" +"🌙   Вечір   " + arr1[3] + "\n"
#         await message.answer(stra)
#     print(message.from_user.id)


    #-------------------------------------------------------------------------------------------------


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=["start"])
    dp.register_message_handler(weather1, commands=["погода_сьогодні"])
    dp.register_message_handler(weather2, commands=["погода_завтра"])
    dp.register_message_handler(weather3, commands=["погода_після_завтра"])
    dp.register_message_handler(weather4, commands=["погода_через_2_дні"])
    dp.register_message_handler(all_cities, commands=["all_cities"])
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
