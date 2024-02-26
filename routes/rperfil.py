from fastapi import APIRouter, Depends
from controllers.cperfil import *
from models.mperfil import Mperfil
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_perfil = Cperfil()


@router.post("/crear_perfil/")
async def crear_perfil(perfil: Mperfil, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_perfil.crear_perfil(perfil)
    return rpta


@router.get("/obtener_perfil/{perfil_id}",response_model=Mperfil)
async def obtener_perfil(perfil_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_perfil.obtener_perfil(perfil_id)
    return rpta

@router.get("/obtener_perfils/",response_model=List[Mperfil])
async def obtener_perfils(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_perfil.obtener_perfils()
    return rpta

@router.put("/actualizar_perfil/")
async def actualizar_perfil(perfil: Mperfil, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_perfil.actualizar_perfil(perfil)
    return rpta