from fastapi import APIRouter, Depends
from controllers.cevaluacionadmon import *
from models.mevaluacionadmon import Mevaluacionadmon
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_evaluacionadmon = Cevaluacionadmon()


@router.post("/crear_evaluacionadmon/")
async def crear_evaluacionadmon(evaluacionadmon: Mevaluacionadmon, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_evaluacionadmon.crear_evaluacionadmon(evaluacionadmon)
    return rpta


@router.get("/obtener_evaluacionadmon/{evaluacionadmon_id}", response_model=Mevaluacionadmon)
async def obtener_evaluacionadmon(evaluacionadmon_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_evaluacionadmon.obtener_evaluacionadmon(evaluacionadmon_id)
    return rpta

@router.get("/obtener_evaluacionadmons/", response_model=List[Mevaluacionadmon])
async def obtener_evaluacionadmons(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_evaluacionadmon.obtener_evaluacionadmons()
    return rpta


@router.put("/actualizar_evaluacionadmon/")
async def actualizar_evaluacionadmon(evaluacionadmon: Mevaluacionadmon, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_evaluacionadmon.actualizar_evaluacionadmon(evaluacionadmon)
    return rpta