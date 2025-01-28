from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Element(BaseModel):
    atomic_number: int
    name: str
    symbol: str
    description: str

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/load")
def load():
    elements = []
    with open("elements.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
        for element in data:
            elements.append(Element(
                atomic_number=element["atomic_number"],
                name=element["name"],
                symbol=element["symbol"],
                description=element["description"]
            ))
    return elements