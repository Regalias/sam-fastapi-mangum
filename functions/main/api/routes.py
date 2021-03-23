
from fastapi import FastAPI
from starlette.requests import Request
from . import lib

app = FastAPI(openapi_url=None)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/echo")
def echo_handler(request: Request):
    return {"ip": f"{lib.get_ip(request)}"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}