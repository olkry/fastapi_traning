from datetime import datetime
from typing import NamedTuple, Annotated

from fastapi import FastAPI, Depends, HTTPException


app = FastAPI()


class Settings(NamedTuple):
    cucuphone_limit: int
    hour_open: int
    hour_close: int


def get_settings():
    return Settings(cucuphone_limit=2, hour_open=8, hour_close=22)


# Здесь опишите объект SettingsDep.
SettingsDep = Annotated[Settings, Depends(get_settings)]


@app.post("/cucuphone")
async def buy_cucuphone(
    quantity: int,
    settings: SettingsDep,
) -> dict:
    # Тут проверьте, не превышено ли в заказе разрешённое количество смартфонов.
    # Верните сообщение об успешном заказе или выбросьте исключение с кодом 400.
    if quantity > settings.cucuphone_limit:
        raise HTTPException(
            status_code=400,
            detail='Привышен лимит телефонов для единичного заказа'
        )
    return {'detail': 'Спасибо, ваш заказ зарегистрирован!'}


@app.get("/is-store-open")
async def is_store_open(
    settings: SettingsDep,
) -> bool:
    hour_now = datetime.now().hour
    # Проверьте, попадает ли текущее время в диапазон
    # между открытием и закрытием магазина.
    # В зависимости от результата проверки
    # верните True (это значит "открыто") или False (это значит "закрыто").
    if settings.hour_open <= hour_now < settings.hour_close:
        return True
    return False
