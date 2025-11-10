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


print(100 - 100.0 * (50.5 / 100.0))
