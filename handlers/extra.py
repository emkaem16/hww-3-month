from aiogram import types, Dispatcher


from config import bot, dp





@dp.message_handler()
async def echo(message: types.Message):
    if message.text.startswith("!pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text.lower() == "game":
        await bot.send_game(message.chat.id, emoji='⚽')
        await bot.send_game(message.chat.id, emoji='🏀')
        await bot.send_game(message.chat.id, emoji='🎲')
        await bot.send_game(message.chat.id, emoji='🎯')
        await bot.send_game(message.chat.id, emoji='🎳')
        await bot.send_game(message.chat.id, emoji='🎰')






def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)