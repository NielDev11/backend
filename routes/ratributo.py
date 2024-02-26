from fastapi import APIRouter, Depends
from controllers.catributo import *
from models.matributo import Matributo
from typing import List
from auth.auth_route import protected_route
router = APIRouter()

nuevo_atributo = Catributo()


@router.post("/crear_atributo/")
async def crear_atributo(atributo: Matributo, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_atributo.crear_atributo(atributo)
    return rpta


@router.get("/obtener_atributo/{atributo_id}",response_model=Matributo)
async def obtener_atributo(atributo_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_atributo.obtener_atributo(atributo_id)
    return rpta

@router.get("/obtener_atributos/",response_model=List[Matributo])
async def obtener_atributos(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_atributo.obtener_atributos()
    return rpta

@router.put("/actualizar_atributo/")
async def actualizar_atributo(atributo: Matributo, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_atributo.actualizar_atributo(atributo)
    return rpta