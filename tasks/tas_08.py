from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict

app = FastAPI()


class IncomingMessage(BaseModel):
    # Модифицируйте атрибуты, чтобы они соответствовали заданию.
    title: Optional[str] = Field('У этого сообщения нет заголовка',)
    body: str = Field(min_length=1,)
    contacts: Optional[str] = Field(None,)
    secret_hash: str = Field(min_length=1,)


class OutgoingMessage(BaseModel):
    # Опишите класс исходящего сообщения.
    title: Optional[str] = Field('У этого сообщения нет заголовка',)
    body: str
    contacts: Optional[str] = Field(None,)

    model_config = ConfigDict(from_attributes=True)


# Модифицируйте эндпоинт так,
# чтобы он выполнял поставленную задачу.
@app.post(
    '/post-office',
    response_model=OutgoingMessage,
    response_model_exclude_defaults=True,
    response_model_exclude_none=True,
    response_model_exclude_unset=True
)
def sloth(message: IncomingMessage):
    # Отсюда можно передать данные для обработки и сохранения в БД,
    # но этого писать мы не будем. И вам не нужно.
    return message
