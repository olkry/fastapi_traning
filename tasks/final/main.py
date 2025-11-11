from fastapi import FastAPI

from tasks.final.api import router


app = FastAPI()
app.include_router(router)
