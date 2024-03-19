from fastapi import APIRouter, Depends
from controllers.ccargo import *
from models.mcargo import Mcargo
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_cargo = Ccargo()


@router.post("/crear_cargo/")
async def crear_cargo(cargo: Mcargo, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_cargo.crear_cargo(cargo)
    return rpta


@router.get("/obtener_cargo/{cargo_id}")
async def obtener_cargo(cargo_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_cargo.obtener_cargo(cargo_id)
    return rpta


@router.get("/obtener_cargos/")
async def obtener_cargos(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_cargo.obtener_cargos()
    return rpta


@router.put("/actualizar_cargo/")
async def actualizar_cargo(cargo: Mcargo, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_cargo.actualizar_cargo(cargo)
    return rpta

@router.put("/deshabilitar_cargo/{cargo_id}")
async def deshabilitar_cargo(cargo_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_cargo.deshabilitar_cargo(cargo_id)
    return rpta

@router.put("/activar_cargo/{cargo_id}")
async def activar_cargo(cargo_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_cargo.activar_cargo(cargo_id)
    return rpta