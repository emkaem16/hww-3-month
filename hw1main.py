from aiogram.utils import executor

from config import bot, dp
from handlers import client, admin, callback, extra
import logging

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
extra.register_handlers_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)