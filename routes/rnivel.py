from fastapi import APIRouter, Depends
from controllers.cnivel import *
from models.mnivel import Mnivel
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_nivel = Cnivel()

@router.post("/crear_nivel/")
async def crear_nivel(nivel: Mnivel, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_nivel.crear_nivel(nivel)
    return rpta

@router.get("/obtener_nivel/{nivel_id}", response_model=Mnivel)
async def obtener_nivel(nivel_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_nivel.obtener_nivel(nivel_id)
    return rpta

@router.get("/obtener_niveles/", response_model=List[Mnivel])
async def obtener_niveles(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_nivel.obtener_niveles()
    return rpta

@router.put("/actualizar_nivel/")
async def actualizar_nivel(nivel: Mnivel, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_nivel.actualizar_nivel(nivel)
    return rpta

@router.put("/deshabilitar_nivel/{nivel_id}")
async def deshabilitar_nivel(nivel_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_nivel.deshabilitar_nivel(nivel_id)
    return rpta

@router.put("/activar_nivel/{nivel_id}")
async def activar_nivel(nivel_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_nivel.activar_nivel(nivel_id)
    return rpta
