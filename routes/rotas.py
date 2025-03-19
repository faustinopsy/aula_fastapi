from fastapi import APIRouter
from typing import Union

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Olá, mundo com FastAPI!"}

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@router.post("/items")
async def create_item(item: dict):
    return {"message": "Recurso criado", "item": item}

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"message": f"Recurso {item_id} atualizado", "item": item}

@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Recurso {item_id} removido"}