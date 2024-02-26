from fastapi import APIRouter, HTTPException
from controllers.ctipoevaluacion import *
from models.mtipoevaluacion import Mtipoevaluacion
from typing import List

router = APIRouter()

nuevo_tipoevaluacion = Ctipoevaluacion()


@router.post("/crear_tipoevaluacion/")
async def crear_tipoevaluacion(tipoevaluacion: Mtipoevaluacion):
    rpta = nuevo_tipoevaluacion.crear_tipoevaluacion(tipoevaluacion)
    return rpta


@router.get("/obtener_tipoevaluacion/{tipoevaluacion_id}",response_model=Mtipoevaluacion)
async def obtener_tipoevaluacion(tipoevaluacion_id: int):
    rpta = nuevo_tipoevaluacion.obtener_tipoevaluacion(tipoevaluacion_id)
    return rpta

@router.get("/obtener_tipoevaluacions/",response_model=List[Mtipoevaluacion])
async def obtener_tipoevaluacions():
    rpta = nuevo_tipoevaluacion.obtener_tipoevaluacions()
    return rpta

@router.put("/actualizar_tipoevaluacion/")
async def actualizar_tipoevaluacion(tipoevaluacion: Mtipoevaluacion):
    rpta = nuevo_tipoevaluacion.actualizar_tipoevaluacion(tipoevaluacion)
    return rpta