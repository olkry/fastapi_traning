# import datetime
from enum import StrEnum
from typing import Annotated

from fastapi import FastAPI, Path, Query
import uvicorn

app = FastAPI()
# app = FastAPI(docs_url=None, redoc_url=None)  # Залочить документации


class EducationLevel(StrEnum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


# Декоратор, определяющий, что GET-запросы к основному URL приложения
# должны обрабатываться этой функцией.
@app.get('/')
async def read_root():
    """Главная страница."""
    return {'Hello': 'FastAPI'}
    # return datetime.datetime.now()


@app.get('/me', tags=['special methods'], summary='Приветствие автора')
async def hello_author():
    return {'Hello': 'dear author'}


@app.get(
    '/{name}',
    tags=['common methods'],
    summary='Общее приветствие',
    # description='Приветствие человека по имени и фамилии; '
    #             'опционально указывается возраст, '
    #             'образование и статус сотрудника',
    response_description='Полная строка приветствия'
)
async def greetings(
        name: Annotated[str, Path(min_length=2, max_length=20)],
        surname: Annotated[str, Query(min_length=2, max_length=50)],
        # gt означает "больше", >; le — "меньше или равно", <=.
        # gt:  больше чем (greater than), >;
        # ge:  больше чем или равно (greater than or equal), >=;
        # lt:  меньше чем (less than), <;
        # le:  меньше чем или равно (less than or equal), <=.
        age: Annotated[int | None, Query(gt=4, lt=100)] = None,
        is_staff: bool = False,
        education_level: EducationLevel = None,
) -> dict[str, str]:
    """
    Приветствие пользователя:

    - **name**: имя
    - **surname**: фамилия
    - **age**: возраст (опционально)
    - **is_staff**: является ли пользователь сотрудником
    - **education_level**: уровень образования (опционально)
    """
    result = ' '.join([name, surname])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)

    if education_level is not None:
        result += ', ' + education_level.lower()

    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

# Запуск сервера с авторелодом uvicorn main:app --reload
