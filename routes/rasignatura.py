from fastapi import APIRouter, HTTPException, Depends
from controllers.casignatura import *
from models.masignatura import Masignatura
from auth.auth_route import protected_route
from typing import List

router = APIRouter()

nuevo_asignatura = Casignatura()


@router.post("/crear_asignatura/")
async def crear_asignatura(asignatura: Masignatura, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_asignatura.crear_asignatura(asignatura)
    return rpta

@router.get("/obtener_asignatura/{asignatura_id}",response_model=Masignatura)
async def obtener_asignatura(asignatura_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_asignatura.obtener_asignatura(asignatura_id)
    return rpta

@router.get("/obtener_asignaturas/",response_model=List[Masignatura])
async def obtener_asignaturas(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_asignatura.obtener_asignaturas()
    return rpta

@router.put("/actualizar_asignatura/")
async def actualizar_asignatura(asignatura: Masignatura, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_asignatura.actualizar_asignatura(asignatura)
    return rpta
