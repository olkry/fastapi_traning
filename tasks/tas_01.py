from fastapi import FastAPI

app = FastAPI()


# Укажите и аннотируйте параметры функции.
# Аннотируйте тип возвращаемого значения функции.
@app.get('/multiplication')
async def multiplication(
    length: int,
    width: int,
    depth: int | None = None
) -> int:
    result = length * width
    if depth is not None:
        result *= depth
    return result

# Реализуйте логику функции
# и верните результат.