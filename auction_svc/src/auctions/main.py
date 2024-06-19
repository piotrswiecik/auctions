from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "root"}

@app.get("/test1")
def test1():
    return {"message": "test1"}