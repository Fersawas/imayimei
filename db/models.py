from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declarative_base


class Base(AsyncAttrs,DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    @declared_attr.directive
    def __tablename__(cls):
        return cls.__name__.lower() + 's'


class WhiteList(Base):

    user_id: Mapped[int] = mapped_column(Integer, unique=True) 
    name: Mapped[str] = mapped_column(String(150))
