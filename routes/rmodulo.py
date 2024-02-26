from fastapi import APIRouter, Depends
from controllers.cmodulo import *
from models.mmodulo import Mmodulo
from typing import List
from auth.auth_route import protected_route


router = APIRouter()

nuevo_modulo = Cmodulo()


@router.post("/crear_modulo/")
async def crear_modulo(modulo: Mmodulo, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_modulo.crear_modulo(modulo)
    return rpta


@router.get("/obtener_modulo/{modulo_id}",response_model=Mmodulo)
async def obtener_modulo(modulo_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_modulo.obtener_modulo(modulo_id)
    return rpta

@router.get("/obtener_modulos/",response_model=List[Mmodulo])
async def obtener_modulos(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_modulo.obtener_modulos()
    return rpta

@router.put("/actualizar_modulo/")
async def actualizar_modulo(modulo: Mmodulo, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_modulo.actualizar_modulo(modulo)
    return rpta