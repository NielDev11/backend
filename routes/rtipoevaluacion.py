from fastapi import APIRouter, Depends
from controllers.ctipoevaluacion import *
from models.mtipoevaluacion import Mtipoevaluacion
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_tipoevaluacion = Ctipoevaluacion()


@router.post("/crear_tipoevaluacion/")
async def crear_tipoevaluacion(tipoevaluacion: Mtipoevaluacion, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_tipoevaluacion.crear_tipoevaluacion(tipoevaluacion)
    return rpta


@router.get("/obtener_tipoevaluacion/{tipoevaluacion_id}")
async def obtener_tipoevaluacion(tipoevaluacion_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_tipoevaluacion.obtener_tipoevaluacion(tipoevaluacion_id)
    return rpta

@router.get("/obtener_tipoevaluacions/")
async def obtener_tipoevaluacions(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_tipoevaluacion.obtener_tipoevaluacions()
    return rpta

@router.put("/actualizar_tipoevaluacion/")
async def actualizar_tipoevaluacion(tipoevaluacion: Mtipoevaluacion, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_tipoevaluacion.actualizar_tipoevaluacion(tipoevaluacion)
    return rpta

@router.put("/deshabilitar_tipoevaluacion/{tipoevaluacion_id}")
async def deshabilitar_tipoevaluacion(tipoevaluacion_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_tipoevaluacion.deshabilitar_tipoevaluacion(tipoevaluacion_id)
    return rpta

@router.put("/activar_tipoevaluacion/{tipoevaluacion_id}")
async def activar_tipoevaluacion(tipoevaluacion_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_tipoevaluacion.activar_tipoevaluacion(tipoevaluacion_id)
    return rpta