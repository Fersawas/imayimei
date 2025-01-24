#!/bin/bash

# Применяем миграции Alembic
echo "Applying Alembic migrations..."
alembic upgrade head

# Запускаем бота
echo "Starting the bot..."
python bot.py