from fastapi import APIRouter, Depends
from controllers.cgrupo import *
from models.mgrupo import Mgrupo
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_grupo = Cgrupo()


@router.post("/crear_grupo/")
async def crear_grupo(grupo: Mgrupo, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_grupo.crear_grupo(grupo)
    return rpta


@router.get("/obtener_grupo/{grupo_id}", response_model=Mgrupo)
async def obtener_grupo(grupo_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_grupo.obtener_grupo(grupo_id)
    return rpta


@router.get("/obtener_grupos/", response_model=List[Mgrupo])
async def obtener_grupos(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_grupo.obtener_grupos()
    return rpta


@router.put("/actualizar_grupo/")
async def actualizar_grupo(grupo: Mgrupo, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_grupo.actualizar_grupo(grupo)
    return rpta