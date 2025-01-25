from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from sqlalchemy.future import select

from db.database import async_session_maker
from db.models import WhiteList
from constants import MESSAGES


router = Router()


async def check_user(user_id: int) -> bool:
    '''
    Проверка наличия пользователя в бд
    '''

    async with async_session_maker() as session:
        query = await session.execute(select(WhiteList).filter(WhiteList.user_id == user_id))
    return query.scalar() is not None


@router.message(Command('add_me'))
async def add_me(message: Message):
    '''
    Функция добавления пользователя в бд
    '''

    async with async_session_maker() as session:
        query = select(WhiteList).where(WhiteList.user_id == message.from_user.id)
        result = await session.execute(query)
        existing_user = result.scalars().first()
        if existing_user:
            await message.answer(MESSAGES['in_club'])
            return
        new_user = WhiteList(user_id=message.from_user.id,
                             name=message.from_user.first_name)
        
        session.add(new_user)
        await session.commit()

    await message.answer(MESSAGES['first_in_club'])


@router.message(Command('remove_me'))
async def remove_me(message: Message):
    '''
    Функция удаления пользователя из бд
    '''
    async with async_session_maker() as session:
        query = select(WhiteList).where(WhiteList.user_id == message.from_user.id)
        result = await session.execute(query)
        existing_user = result.scalars().first()
        if existing_user:
            await session.delete(existing_user)
            await session.commit()
            await message.answer(MESSAGES['removed_from_club'])
        else:
            await message.answer(MESSAGES['not_in_club'])

