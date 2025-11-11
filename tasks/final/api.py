from typing import Annotated

from fastapi import APIRouter, Body

from tasks.final.schemas import Bulletin

router = APIRouter()


@router.post('/the-most-fair-voting')
async def choose_framework(voice: Annotated[Bulletin, Body()]):
    # Whatever you choose.
    return {'The winner is': 'FastAPI'}
