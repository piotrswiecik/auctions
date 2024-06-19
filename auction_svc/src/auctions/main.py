import logging

from fastapi import FastAPI

from auctions.config import settings
from auctions.seed import init_db

logging.basicConfig(level=logging.INFO)


def create_app() -> FastAPI:
    instance = FastAPI()

    if settings.init_db:
        init_db()

    return instance


app = create_app()


@app.get("/api/auctions/")
async def root():
    return {"message": "hello from auctions"}
