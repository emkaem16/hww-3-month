from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_button = KeyboardButton("/start")
question_button = KeyboardButton("/question")
mem_button = KeyboardButton("/mem")


start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_markup.row(start_button, question_button, mem_button)

