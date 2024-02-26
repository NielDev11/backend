from fastapi import APIRouter, Depends
from controllers.cevaluaciondoc import *
from models.mevaluaciondoc import Mevaluaciondoc
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_evaluaciondoc = Cevaluaciondoc()


@router.post("/crear_evaluaciondoc/")
async def crear_evaluaciondoc(evaluaciondoc: Mevaluaciondoc, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_evaluaciondoc.crear_evaluaciondoc(evaluaciondoc)
    return rpta


@router.get("/obtener_evaluaciondoc/{evaluaciondoc_id}",response_model=Mevaluaciondoc)
async def obtener_evaluaciondoc(evaluaciondoc_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_evaluaciondoc.obtener_evaluaciondoc(evaluaciondoc_id)
    return rpta

@router.get("/obtener_evaluaciondocs/",response_model=List[Mevaluaciondoc])
async def obtener_evaluaciondocs(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_evaluaciondoc.obtener_evaluaciondocs()
    return rpta

@router.put("/actualizar_evaluaciondoc/")
async def actualizar_evaluaciondoc(evaluaciondoc: Mevaluaciondoc, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_evaluaciondoc.actualizar_evaluaciondoc(evaluaciondoc)
    return rpta