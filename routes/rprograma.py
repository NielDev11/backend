from fastapi import APIRouter, Depends
from controllers.cprograma import *
from models.mprograma import Mprograma
from typing import List
from auth.auth_route import protected_route
router = APIRouter()

nuevo_programa = Cprograma()


@router.post("/crear_programa/")
async def crear_programa(programa: Mprograma, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_programa.crear_programa(programa)
    return rpta


@router.get("/obtener_programa/{programa_id}")
async def obtener_programa(programa_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_programa.obtener_programa(programa_id)
    return rpta

@router.get("/obtener_programas/")
async def obtener_programas(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_programa.obtener_programas()
    return rpta

@router.put("/actualizar_programa/")
async def actualizar_programa(programa: Mprograma, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_programa.actualizar_programa(programa)
    return rpta

@router.put("/deshabilitar_programa/{programa_id}")
async def deshabilitar_programa(programa_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_programa.deshabilitar_programa(programa_id)
    return rpta

@router.put("/activar_programa/{programa_id}")
async def activar_programa(programa_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_programa.activar_programa(programa_id)
    return rpta