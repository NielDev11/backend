from fastapi import APIRouter, Depends
from controllers.ccompetencia import *
from models.mcompetencia import Mcompetencia
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_competencia = Ccompetencia()


@router.post("/crear_competencia/")
async def crear_competencia(competencia: Mcompetencia, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_competencia.crear_competencia(competencia)
    return rpta


@router.get("/obtener_competencia/{competencia_id}", response_model=Mcompetencia)
async def obtener_competencia(competencia_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_competencia.obtener_competencia(competencia_id)
    return rpta


@router.get("/obtener_competencias/", response_model=List[Mcompetencia])
async def obtener_competencias(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_competencia.obtener_competencias()
    return rpta


@router.put("/actualizar_competencia/")
async def actualizar_competencia(competencia: Mcompetencia, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_competencia.actualizar_competencia(competencia)
    return rpta
