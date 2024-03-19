from fastapi import APIRouter, Depends
from controllers.cusuario import *
from models.musuario import Musuario
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_usuario = Cusuario()


@router.post("/crear_usuario/")
async def crear_usuario(usuario: Musuario, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_usuario.crear_usuario(usuario)
    return rpta

@router.get("/obtener_usuario/{usuario_id}",response_model=Musuario)
async def obtener_usuario(usuario_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_usuario.obtener_usuario(usuario_id)
    return rpta

@router.get("/obtener_usuarios/")
async def obtener_usuarios(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_usuario.obtener_usuarios()
    return rpta

@router.put("/actualizar_usuario/")
async def actualizas_usuario(usuario: Musuario, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_usuario.actualizar_usuario(usuario)
    return rpta

@router.put("/eliminar_usuario/{usuario_id}")
async def eliminar_usuario(usuario_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_usuario.eliminar_usuario(usuario_id)
    return rpta

@router.put("/activar_usuario/{usuario_id}")
async def activar_usuario(usuario_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_usuario.activar_usuario(usuario_id)
    return rpta