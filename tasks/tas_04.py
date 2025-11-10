from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/price-tag')
async def get_price_tag(
    name: Annotated[str, Query(min_length=2)],
    original_price: Annotated[float, Query(ge=1.0, le=1000.0)],
    discount: Annotated[float | None, Query(ge=10.0, le=99.0)] = None
) -> dict:
    if len(name) > 25:
        name = name[:22] + '...'
    new_price = original_price
    if discount is not None:
        new_price = round(original_price - original_price * (discount / 100), 2)
    return {
        'name': name,
        'original_price': original_price,
        'new_price': new_price
    }
