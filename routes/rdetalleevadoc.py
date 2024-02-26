from fastapi import APIRouter, Depends
from controllers.cdetalleevadoc import *
from models.mdetalleevadoc import Mdetalleevadoc
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_detalleevadoc = Cdetalleevadoc()


@router.post("/crear_detalleevadoc/")
async def crear_detalleevadoc(detalleevadoc: Mdetalleevadoc, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_detalleevadoc.crear_detalleevadoc(detalleevadoc)
    return rpta


@router.get("/obtener_detalleevadoc/{detalleevadoc_id}", response_model=Mdetalleevadoc)
async def obtener_detalleevadoc(detalleevadoc_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_detalleevadoc.obtener_detalleevadoc(detalleevadoc_id)
    return rpta


@router.get("/obtener_detalleevadocs/", response_model=List[Mdetalleevadoc])
async def obtener_detalleevadocs(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_detalleevadoc.obtener_detalleevadocs()
    return rpta


@router.put("/actualizar_detalleevadoc/")
async def actualizar_detalleevadoc(detalleevadoc: Mdetalleevadoc, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_detalleevadoc.actualizar_detalleevadoc(detalleevadoc)
    return rpta
