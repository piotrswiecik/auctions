from fastapi import FastAPI

app = FastAPI()


@app.get("/api/search")
def root():
    return {"message": "hello from search"}
