from typing import Self

from fastapi import FastAPI
from pydantic import BaseModel, model_validator

app = FastAPI()

FORBIDDEN_NAMES = [
    'Luke Skywalker',
    'Darth Vader',
    'Leia Organa',
    'Han Solo',
]


class Person(BaseModel):
    name: str
    surname: str

    @model_validator(mode='after')
    def not_forbidden_names(self) -> Self:
        check_value = self.name + ' ' + self.surname
        if check_value.title() in FORBIDDEN_NAMES:
            error = 'Такое сочетание запрещено'
            raise ValueError(error)
        return self



@app.post('/hello')
async def greetings(person: Person) -> dict[str, str]:
    result = ' '.join([person.name, person.surname])
    result = result.title()
    return {'Hello': result}