from fastapi import FastAPI

app = FastAPI()


@app.get("/api/auctions/")
def root():
    return {"message": "hello from auctions"}


print()
print()
print()
print()
print()
