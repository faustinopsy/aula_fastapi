from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Olá, mundo com FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items")
async def create_item(item: dict):
    return {"message": "Recurso criado", "item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"message": f"Recurso {item_id} atualizado", "item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Recurso {item_id} removido"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)