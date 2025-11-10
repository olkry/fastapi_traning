from random import randint, choice
from secrets import token_hex
from uuid import uuid4
from enum import StrEnum

from fastapi import FastAPI

app = FastAPI()


class Tag(StrEnum):
    FRONT = 'Для фронтендера'
    BACK = 'Для бэкендера'
    FOR_ALL = 'Для всех'


@app.get(
    '/hexcolor',
    tags=[Tag.FRONT],
    summary='Кодировка цвета в HEX',
    description='Возвращает код цвета в формате HEX',
    response_description='Строка HEX кода (например #32a852)'
)
async def get_hex_color() -> str:
    return f'#{token_hex(3)}'


@app.get(
    '/uuid',
    tags=[Tag.BACK],
    summary='Генерация UUIDv4',
    description='возвращает случайный уникальный идентификатор UUIDv4',
    response_description='Строка идентификатор UUIDv4'
)
async def get_random_uuid() -> str:
    return str(uuid4())


HELLO_WORLD_LIST = [
    'Hello world',
    'Hola mundo',
    'Bonjour le monde',
    'Hallo Welt',
    'Ciao mondo',
    'Olá mundo',
    'Привет мир',
    'こんにちは世界',
    '你好世界',
    'مرحبا بالعالم'
]


@app.get(
    '/helloworld',
    tags=[Tag.BACK],
    summary='Разнообразное приветствие',
    description='возвращает фразу “Hello world” на случайно выбранном языке',
    response_description='Строка с приветствием'
)
async def get_hello_world() -> str:
    return choice(HELLO_WORLD_LIST)


@app.get(
    '/dumplings',
    tags=[Tag.FOR_ALL],
    summary='Сколько пельмешей бахнуть',
    description='возвращает количество пельменей, '
    'которые следует сварить для поддержания сил',
    response_description='Числовое количество'
)
async def get_dumplings_count() -> int:
    return randint(5, 20)


@app.get(
    '/coin',
    tags=[Tag.FOR_ALL],
    summary='Сколько пельмешей бахнуть',
    description='«подбрасывает монетку» и возвращает True или False на случай,'
    ' если надо принять важное решение',
    response_description='Булево значение'
)
async def toss_a_coin() -> bool:
    return choice([True, False])
