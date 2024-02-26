from fastapi import APIRouter, Depends
from controllers.cmoduloxperfil import *
from models.mmoduloxperfil import Mmoduloxperfil
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_moduloxperfil = Cmoduloxperfil()


@router.post("/crear_moduloxperfil/")
async def crear_moduloxperfil(moduloxperfil: Mmoduloxperfil, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_moduloxperfil.crear_moduloxperfil(moduloxperfil)
    return rpta

@router.get("/obtener_moduloxperfil/{moduloxperfil_id}",response_model=Mmoduloxperfil)
async def obtener_moduloxperfil(moduloxperfil_id: int, get_protected_route: dict = Depends(protected_route) ):
    rpta = nuevo_moduloxperfil.obtener_moduloxperfil(moduloxperfil_id)
    return rpta

@router.get("/obtener_moduloxperfils/",response_model=List[Mmoduloxperfil])
async def obtener_moduloxperfils(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_moduloxperfil.obtener_moduloxperfils()
    return rpta

@router.put("/actualizar_moduloxperfil/")
async def actualizar_moduloxperfil(moduloxperfil: Mmoduloxperfil, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_moduloxperfil.actualizar_moduloxperfil(moduloxperfil)
    return rpta