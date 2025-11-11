from enum import StrEnum

from pydantic import BaseModel


class PythonFramework(StrEnum):
    DJANGO = 'Django'
    FASTAPI = 'FastAPI'
    FLASK = 'Flask'
    PYRAMID = 'Pyramid'
    QUART = 'Quart'
    SANIC = 'Sanic'
    TORNADO = 'Tornado'


class Bulletin(BaseModel):
    framework: PythonFramework
    your_name: str
