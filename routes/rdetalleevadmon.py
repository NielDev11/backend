from fastapi import APIRouter, Depends
from controllers.cdetalleevadmon import *
from models.mdetalleevadmon import Mdetalleevadmon
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_detalleevadmon = Cdetalleevadmon()


@router.post("/crear_detalleevadmon/")
async def crear_detalleevadmon(detalleevadmon: Mdetalleevadmon, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_detalleevadmon.crear_detalleevadmon(detalleevadmon)
    return rpta


@router.get(
    "/obtener_detalleevadmon/{detalleevadmon_id}", response_model=Mdetalleevadmon
)
async def obtener_detalleevadmon(detalleevadmon_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_detalleevadmon.obtener_detalleevadmon(detalleevadmon_id)
    return rpta


@router.get("/obtener_detalleevadmons/", response_model=List[Mdetalleevadmon])
async def obtener_detalleevadmons(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_detalleevadmon.obtener_detalleevadmons()
    return rpta


@router.put("/actualizar_detalleevadmon/")
async def actualizar_detalleevadmon(detalleevadmon: Mdetalleevadmon, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_detalleevadmon.actualizar_detalleevadmon(detalleevadmon)
    return rpta
