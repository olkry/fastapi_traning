# from enum import Enum


# class Fruit(Enum):
#     # Синтаксис: имя = значение.
#     # Значения элементов в классе Enum - неизменяемые,
#     # следовательно, имена - это константы.
#     # Имена констант по PEP 8 пишутся большими буквами.
#     APPLE = 110
#     PEAR = 128
#     PLUM = 256


# print(Fruit.APPLE.value)
# print(Fruit.APPLE)
# print(Fruit(110))
# print(Fruit(110).name)
# print(80 / 100)

# 110
# Fruit.APPLE
# Fruit.APPLE
# APPLE

# from enum import StrEnum

# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()


# class EducationLevel(StrEnum):
#     SECONDARY = 'Среднее образование'
#     SPECIAL = 'Среднее специальное образование'
#     HIGHER = 'Высшее образование'


# @app.get('/{name}')
# async def greetings(
#         name: str,
#         surname: str,
#         age: int | None = None,
#         is_staff: bool = False,
#         education_level: EducationLevel | None = None,
# ) -> dict[str, str]:
#     result = ' '.join([name, surname])
#     result = result.title()
#     if age is not None:
#         result += ', ' + str(age)

#     if education_level is not None:
#         result += ', ' + education_level.lower()

#     if is_staff:
#         result += ', сотрудник'
#     return {'Hello': result}

# name = 'Han Solo'
# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.capitalize())
# print(name)

""" Структура примерная большого проекта

big_online_market/
    └── app/
        ├── api/                # Тут все функции-обработчики проекта.
        |   ├── __init__.py
        |   ├── customer.py
        |   ├── order.py
        |   └── shop.py
        ├── сore/                # Тут "ядро" проекта.
        |   ├── __init__.py
        |   ├── config.py
        |   └── db.py
        ├── models/              # Тут все модели проекта.
        |   ├── __init__.py
        |   ├── customer.py
        |   ├── order.py
        |   └── shop.py
        ├── schemas/              # Тут все схемы проекта.
        |   ├── __init__.py
        |   ├── customer.py
        |   ├── order.py
        |   └── shop.py
        ├── service/              # Тут бизнес-логика проекта.
        |   ├── __init__.py
        |   ├── matching.py
        |   └── security_checks.py
        ├── __init__.py
        └── main.py               # Тут создаётся объект приложения. 

Или так:

big_online_market/
    └── app/
        ├── catalog/              # Тут файлы для управления каталогом.
        |   ├── __init__.py
        |   ├── schemas.py
        |   ├── models.py
        |   ├── matching.py      # Тут логика, относящаяся только к catalog/        
        |   └── endpoints.py
        ├── сore/                # Тут "ядро" проекта.
        |   ├── __init__.py
        |   ├── config.py
        |   └── db.py
        ├── order/                # Тут файлы для работы с заказом.
        |   ├── __init__.py
        |   ├── schemas.py
        |   ├── models.py
        |   └── endpoints.py
        ├── user/                 # Тут файлы для работы с пользователями.
        |   ├── __init__.py
        |   ├── schemas.py
        |   ├── models.py
        |   ├── security_checks.py  # Тут логика, относящаяся только к user/     
        |   └── endpoints.py
          ├── __init__.py
          └── main.py               # Тут создаётся объект приложения. 


Маленький проект примерно так:
small_offline_market/
    └── app/
          ├── __init__.py
        ├── api.py
        ├── logic.py        
          ├── main.py
        ├── models.py
        ├── security.py        
          └── schemas.py 
"""

