import re
from enum import Enum
from typing import Optional, Union, Self

from pydantic import (
    BaseModel, Field, ConfigDict, field_validator, model_validator
)


class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


class Person(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=20,
        title='Полное имя',
        description='Можно вводить в любом регистре'
    )
    surname: Union[str, list[str]]
    age: Optional[int] = Field(None, gt=4, le=99)
    is_staff: bool = Field(False, alias='is-staff')
    education_level: Optional[EducationLevel] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
    )

    @field_validator('name', 'surname')
    def cannot_be_numbers(cls, value: str):
        assert not value.isnumeric(), 'Имя или фамилия не могут быть числом'
        return value

    @model_validator(mode='after')
    def using_different_languages(self) -> Self:
        surname = ''.join(self.surname)
        checked_value = self.name + surname
        if (re.search('[a-z]', checked_value, re.IGNORECASE)
                and re.search('[а-я]', checked_value, re.IGNORECASE)):
            error = 'Пожалуйста, не смешивайте русские и латинские буквы'
            raise ValueError(error)
        return self
