from aiogram import types, Dispatcher
from config import bot, ADMIN

async def only_admin_pin(message: types.Message):
    if message.chat.type != '!pin':
        if message.from_user.id not in ADMIN:
            await message.answer("")
        if not message.reply_to_message:
            await message.answer("")
        else:
            await message.bot.pin_chat_message(message.chat.id,
                                               user_id=message.reply_to_message.from_user.id)
            await message.answer(f"{message.reply_to_message.from_user.full_name} "
                                 f"{message.from_user}")
    else:
        await message.answer("")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commads_prefix="!/")