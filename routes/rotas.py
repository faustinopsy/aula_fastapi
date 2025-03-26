from fastapi import APIRouter, Request
from controllers import user_controller

router = APIRouter()

@router.get("/")
def pagina_inicial(request: Request):
    return user_controller.mostrar_usuarios(request)

@router.post("/usuarios")
async def cadastrar(request: Request):
    form = await request.form()
    return await user_controller.cadastrar_usuario(request, nome=form["nome"], email=form["email"])

@router.get("/usuarios/delete/{user_id}")
def deletar(user_id: int):
    return user_controller.excluir_usuario(user_id)

@router.get("/usuarios/edit/{user_id}")
def editar_usuario(request: Request, user_id: int):
    return user_controller.mostrar_edicao(request, user_id)

@router.post("/usuarios/update/{user_id}")
async def atualizar(request: Request, user_id: int):
    form = await request.form()
    return await user_controller.atualizar_usuario(request, user_id, nome=form["nome"], email=form["email"])
