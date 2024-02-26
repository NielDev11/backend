from fastapi import APIRouter, Depends
from controllers.ceva_doc_director import *
from models.meva_doc_director import Meva_doc_director
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_eva_doc_director = Ceva_doc_director()


@router.post("/crear_eva_doc_director/")
async def crear_eva_doc_director(eva_doc_director: Meva_doc_director, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_eva_doc_director.crear_eva_doc_director(eva_doc_director)
    return rpta


@router.get(
    "/obtener_eva_doc_director/{eva_doc_director_id}", response_model=Meva_doc_director
)
async def obtener_eva_doc_director(eva_doc_director_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_eva_doc_director.obtener_eva_doc_director(eva_doc_director_id)
    return rpta


@router.get("/obtener_eva_doc_directors/", response_model=List[Meva_doc_director])
async def obtener_eva_doc_directors(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_eva_doc_director.obtener_eva_doc_directors()
    return rpta


@router.put("/actualizar_eva_doc_director/")
async def actualizar_eva_doc_director(eva_doc_director: Meva_doc_director, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_eva_doc_director.actualizar_eva_doc_director(eva_doc_director)
    return rpta