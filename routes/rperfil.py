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

@router.get("/obtener_perfiles/",response_model=List[Mperfil])
async def obtener_perfiles(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_perfil.obtener_perfiles()
    return rpta

@router.get("/obtener_perfiles_activos/")
async def obtener_perfiles_activos(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_perfil.obtener_perfiles_activos()
    return rpta

@router.put("/actualizar_perfil/")
async def actualizar_perfil(perfil: Mperfil, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_perfil.actualizar_perfil(perfil)
    return rpta

@router.put("/deshabilitar_perfil/{perfil_id}")
async def deshabilitar_perfil(perfil_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_perfil.deshabilitar_perfil(perfil_id)
    return rpta

@router.put("/activar_perfil/{perfil_id}")
async def activar_perfil(perfil_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_perfil.activar_perfil(perfil_id)
    return rpta