# IMAYIMEI
## Описание проекта
Бот позволяет выдавать необходимую информацию по вашему imei, при условии, что вы находитесь в белом списке
### Содержанеие

- [Технологии](#tech)
- [Начало работы](#begining)
- [Комнада проекта](#team)

## <a name="tech">Технологии</a>

- [Aiogram](https://aiogram.dev/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## <a name="begining">Начало работы</a>

### Начало работы

Активируйте вирутальное окржуние:

```
python -m venv venv
```

### Установка зависимостей

Установите зависимости из файла *requirements.txt*:

```
pip install -r requirements.txt
```

Если вы работаете локально, в файле .env установите:
*.env*

### Установка зависимостей

Активируйте виртуальное окружение

```
source venv/sqripts/activate
```

Применение миграций и первый запуск:

```
alembic upgrade head
```

### Запуск бота

Запустите проект:

```
python bot.py
```

### Основные команды

/add_me
Добавить себя в белый список

/remove_me
Удалить себя из белого списка

/say_my_name
Попросить бота сказть как вас зовут

/check_imei <int>
Запос к сервису необходимо заполнить поле вашим imei

## <a name="team">Команда проектка</a>

- Паршин Денис - backend developer
