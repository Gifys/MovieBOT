import asyncio
from aiogram import Bot, Dispatcher, executor

from config import TOKEN

loop = asyncio.new_event_loop() # Создаем поток
bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)
