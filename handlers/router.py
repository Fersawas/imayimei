from aiogram import Router
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message

import re

from db_handlers.router import check_user
from api.check import get_imei
from constants import MESSAGES


router = Router()

IMEI_PATTERN = r"^\d{15}$"


def is_valid_imei(imei):
    """
    Проверка валидности imei
    """

    return bool(re.match(IMEI_PATTERN, imei))


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(MESSAGES["start"])


@router.message(Command("say_my_name"))
async def my_name(message: Message):
    await message.answer(f'{MESSAGES["name"]} {message.from_user.first_name}')


@router.message(Command("check_imei"))
async def check_imei(message: Message, command: CommandObject):
    """
    Отправка imei
    """

    imei = command.args
    user_id = message.from_user.id
    if imei:
        if await check_user(user_id):
            if not is_valid_imei(imei):
                await message.answer(MESSAGES["uncorrect_imei"])
            else:
                json_imei = await get_imei(imei)
                await message.answer(json_imei)
        else:
            await message.answer(MESSAGES["not_in_club"])
