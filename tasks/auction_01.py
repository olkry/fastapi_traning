from enum import Enum
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Seller(BaseModel):
    name: str
    surname: str
    country: str


# Создайте класс LotCategory, в котором перечислены 
# разрешённые строковые значения для категорий лотов.
class LotCategory(str, Enum):
    PRINTER = 'Принтеры'
    MONITOR = 'Мониторы'
    ADDON = 'Доп. оборудование'
    INPUTER = 'Устройства ввода'


# Создайте класс AuctionLot, описывающий всю информацию о лоте.
class AuctionLot(BaseModel):
    category: LotCategory
    name: str
    model: Optional[str] = None
    start_price: int = 1000
    seller: Seller


@app.post('/new-lot')
async def register_lot(lot: AuctionLot) -> dict[str, str]:
    result = f'Ваш лот «{lot.name}» зарегистрирован!'
    return {'result': result}
