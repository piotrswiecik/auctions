import logging

from fastapi import Depends, FastAPI

from auctions.config import settings
from auctions.database import get_db
from auctions.repositories import ItemRepository
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


@app.get("/api/auctions/all")
async def get_all(session=Depends(get_db)):
    repo = ItemRepository(session=session)
    items = await repo.get_all()
    logging.info("items: %s", items)
    return {}
