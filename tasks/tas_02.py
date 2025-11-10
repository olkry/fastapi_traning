# Импортируйте нужный класс.
from enum import IntEnum

from fastapi import FastAPI

app = FastAPI()


class OlympicCities(IntEnum):
    CALGARY = 1988
    ALBERTVILLE = 1992
    LILLEHAMMER = 1994
    NAGANO = 1998
    SALT_LAKE_CITY = 2002
    TURIN = 2006
    VANCOUVER = 2010
    SOCHI = 2014
    PYEONGCHANG = 2018
    BEIJING = 2022


@app.get('/get-city')
async def get_olympic_city(item: OlympicCities) -> dict:
    return {'city': item.name,
            'year': item.value}
