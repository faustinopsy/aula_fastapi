from fastapi import APIRouter, Request
from typing import Union
from controllers.ola_controller import ola_mundo
from controllers.responde_html import primeira_pagina

router = APIRouter()

@router.get("/view", response_model=None)
async def chama_template(request: Request):
    return primeira_pagina(request)

@router.get("/")
def read_root():
    return ola_mundo()

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