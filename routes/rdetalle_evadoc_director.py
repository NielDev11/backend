from fastapi import APIRouter, Depends
from controllers.cdetalle_evadoc_director import *
from models.mdetalle_evadoc_director import Mdetalle_evadoc_director
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_detalle_evadoc_director = Cdetalle_evadoc_director()


@router.post("/crear_detalle_evadoc_director/")
async def crear_detalle_evadoc_director(detalle_evadoc_director: Mdetalle_evadoc_director, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_detalle_evadoc_director.crear_detalle_evadoc_director(detalle_evadoc_director)
    return rpta


@router.get("/obtener_detalle_evadoc_director/{detalle_evadoc_director_id}", response_model=Mdetalle_evadoc_director)
async def obtener_detalle_evadoc_director(detalle_evadoc_director_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_detalle_evadoc_director.obtener_detalle_evadoc_director(detalle_evadoc_director_id)
    return rpta


@router.get("/obtener_detalle_evadoc_directors/", response_model=List[Mdetalle_evadoc_director])
async def obtener_detalle_evadoc_directors(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_detalle_evadoc_director.obtener_detalle_evadoc_directors()
    return rpta


@router.put("/actualizar_detalle_evadoc_director/")
async def actualizar_detalle_evadoc_director(detalle_evadoc_director: Mdetalle_evadoc_director, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_detalle_evadoc_director.actualizar_detalle_evadoc_director(detalle_evadoc_director)
    return rpta