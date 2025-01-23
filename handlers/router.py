from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('TEST START')


@router.message(Command('say_my_name'))
async def my_name(message: Message):
    await message.answer(f'Your name is {message.from_user.first_name}')
