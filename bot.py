import os
import asyncio
import logging 

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import load_dotenv

from handlers.router import router


async def main(TOKEN):
    bot = Bot(token=TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main(os.environ['BOT_TOKEN']))  