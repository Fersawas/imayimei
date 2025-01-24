from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from sqlalchemy.future import select

from db.database import async_session_maker
from db.models import WhiteList

router = Router()


@router.message(Command('add_me'))
async def add_me(message: Message):
    print('YEEP')
    async with async_session_maker() as session:
        query = select(WhiteList).where(WhiteList.user_id == message.from_user.id)
        result = await session.execute(query)
        existing_user = result.scalars().first()
        if existing_user:
            await message.answer('Вы уже в клубе')
            return
        new_user = WhiteList(user_id=message.from_user.id,
                             name=message.from_user.first_name)
        
        session.add(new_user)
        await session.commit()

    await message.answer('Первое правило клуба: вы уже в нём')

