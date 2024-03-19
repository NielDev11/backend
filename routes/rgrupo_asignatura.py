from fastapi import APIRouter, HTTPException, Depends
from controllers.cgrupo_asignatura import *
from models.mgrupo_asignatura import Mgrupo_asignatura
from auth.auth_route import protected_route
from typing import List

router = APIRouter()

nuevo_grupo_asignatura = Cgrupo_asignatura()

@router.post("/crear_grupo_asignatura/")
async def crear_grupo_asignatura(grupo_asignatura: Mgrupo_asignatura, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_grupo_asignatura.crear_grupo_asignatura(grupo_asignatura)
    return rpta

@router.get("/obtener_grupo_asignatura/{grupo_asignatura_id}")
async def obtener_grupo_asignatura(grupo_asignatura_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_grupo_asignatura.obtener_grupo_asignatura(grupo_asignatura_id)
    return rpta

@router.get("/obtener_grupo_asignaturas/")
async def obtener_grupo_asignaturas(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_grupo_asignatura.obtener_grupo_asignaturas()
    return rpta

@router.put("/actualizar_grupo_asignatura/")
async def actualizar_grupo_asignatura(grupo_asignatura: Mgrupo_asignatura, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_grupo_asignatura.actualizar_grupo_asignatura(grupo_asignatura)
    return rpta

@router.put("/deshabilitar_grupo_asignatura/{grupo_asignatura_id}")
async def eliminar_grupo_asignatura(grupo_asignatura_id: int, get_protected_route: dict = Depends(protected_route)):
    # nombre = "grupo_asignatura"
    rpta = nuevo_grupo_asignatura.deshabilitar_grupo_asignatura(grupo_asignatura_id)
    return rpta

@router.put("/activar_grupo_asignatura/{grupo_asignatura_id}")
async def activar_grupo_asignatura(grupo_asignatura_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_grupo_asignatura.activar_grupo_asignatura(grupo_asignatura_id)
    return rpta