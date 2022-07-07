from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
weather_now = KeyboardButton("/погода_сьогодні")
weather_now1 = KeyboardButton("/погода_завтра")
weather_now2 = KeyboardButton("/погода_після_завтра")
weather_now3 = KeyboardButton("/погода_через_2_дні")
all_cities_help = KeyboardButton("/all_cities")

kb_client = ReplyKeyboardMarkup()
kb_client_clear = ReplyKeyboardRemove()

kb_client.add(weather_now).add(weather_now1).add(weather_now2).add(weather_now3).add(all_cities_help)