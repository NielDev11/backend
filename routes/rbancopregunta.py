from fastapi import APIRouter, Depends
from controllers.cbancopregunta import *
from models.mbancopregunta import Mbancopregunta
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_bancopregunta = Cbancopregunta()


@router.post("/crear_bancopregunta/")
async def crear_bancopregunta(bancopregunta: Mbancopregunta, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_bancopregunta.crear_bancopregunta(bancopregunta)
    return rpta


@router.get("/obtener_bancopregunta/{bancopregunta_id}", response_model=Mbancopregunta)
async def obtener_bancopregunta(bancopregunta_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_bancopregunta.obtener_bancopregunta(bancopregunta_id)
    return rpta


@router.get("/obtener_bancopreguntas/")
async def obtener_bancopreguntas(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_bancopregunta.obtener_bancopreguntas()
    return rpta


@router.put("/actualizar_bancopregunta/")
async def actualizar_bancopregunta(bancopregunta: Mbancopregunta, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_bancopregunta.actualizar_bancopregunta(bancopregunta)
    return rpta

@router.put("/deshabilitar_bancopregunta/{bancopregunta_id}")
async def deshabilitar_bancopregunta(bancopregunta_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_bancopregunta.deshabilitar_bancopregunta(bancopregunta_id)
    return rpta

@router.put("/activar_bancopregunta/{bancopregunta_id}")
async def activar_bancopregunta(bancopregunta_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_bancopregunta.activar_bancopregunta(bancopregunta_id)
    return rpta