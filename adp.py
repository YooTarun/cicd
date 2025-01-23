from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/greet/{name}")
def greet_user(name: str):
    return {"greeting": f"Hello, {name}!"}

@app.get("/name/{names}")
def print_names(names: str):
    return {"names": names}
