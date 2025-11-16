from fastapi import FastAPI, HTTPException

app = FastAPI()

COMMAND_TO_BOIL = 'Вскипятить воду'


def boil_water():
    pass


@app.post('/samovar_xxi')
def samovar_processing(command: str) -> str:
    if command.lower() != COMMAND_TO_BOIL.lower():
        raise HTTPException(
            status_code=418,
            detail=f'Я же чайник, я не могу {command}!'
        )
    boil_water()
    return 'Вода вскипела!'