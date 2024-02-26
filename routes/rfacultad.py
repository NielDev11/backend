from fastapi import APIRouter, Depends
from controllers.cfacultad import *
from models.mfacultad import Mfacultad
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_facultad = Cfacultad()


@router.post("/crear_facultad/")
async def crear_facultad(facultad: Mfacultad, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_facultad.crear_facultad(facultad)
    return rpta


@router.get("/obtener_facultad/{facultad_id}",response_model=Mfacultad)
async def obtener_facultad(facultad_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_facultad.obtener_facultad(facultad_id)
    return rpta

@router.get("/obtener_facultades/",response_model=List[Mfacultad])
async def obtener_facultades(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_facultad.obtener_facultades()
    return rpta

@router.put("/actualizar_facultad/")
async def actualizar_facultad(facultad: Mfacultad, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_facultad.actualizar_facultad(facultad)
    return rpta