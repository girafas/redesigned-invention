
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/sum")
def sum_numbers(a: int, b: int):
    return {"result": a + b}

@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": a * b}

@app.get("/teste1")
def teste():
    return {"teste": "deu certo"}

@app.get("/novo")
async def novo():
    return {"msg": "branch testes funcionando"}
@app.get("/teste-final")
async def teste_final():
    return {"msg": "funcionando PR"}