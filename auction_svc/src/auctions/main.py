from fastapi import FastAPI

from auctions.config import settings

app = FastAPI()


@app.get("/api/auctions/")
def root():
    return {"message": "hello from auctions"}
