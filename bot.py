import os
import asyncio
import logging
import sys

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
    logging.basicConfig(
    level=logging.DEBUG,  # Уровень логирования
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),  # Вывод логов в stdout
    ],)

    load_dotenv()
    logger = logging.getLogger(__name__)
    try:
        logger.info('start')
        logger.debug('try bot')
        logging.basicConfig(level=logging.DEBUG)
        asyncio.run(main(os.environ['BOT_TOKEN']))
    except Exception as e:
        logger.exception(e)