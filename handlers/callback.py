from aiogram import types, Dispatcher

from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, dp








# @dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def question_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT pidor",
        callback_data='button_call_2',
    )
    markup.add(button_call_2)

    question = 'do you wanna  fruit ice?????'
    answers = [
        "yes",
        "maybe",
        "why not",
        "nup",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def question_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT pidor",
        callback_data='button_call_2',
    )
    markup.add(button_call_2)

    question = 'do you want pizza'
    answers = [
        "yes",
        "maybe",
        "why not",
        "nup",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="if you want you can:)",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )




# @dp.message_handler(commands=['mem'])
async def pic(message: types.Message):
    photo = open("hw_media/photo_2022-06-10_00-01-01.jpg", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(question_2, lambda call: call.data == "button_call_1" )
    dp.register_callback_query_handler(question_3, lambda call: call.data == "button_call_2" )
    dp.register_callback_query_handler(pic, commands=['mem'])