from fastapi import APIRouter, Depends
from controllers.ceva_doc_asig_est import *
from models.meva_doc_asig_est import Meva_doc_asig_est
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_eva_doc_asig_est = Ceva_doc_asig_est()


@router.post("/crear_eva_doc_asig_est/")
async def crear_eva_doc_asig_est(eva_doc_asig_est: Meva_doc_asig_est, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_eva_doc_asig_est.crear_eva_doc_asig_est(eva_doc_asig_est)
    return rpta


@router.get("/obtener_eva_doc_asig_est/{eva_doc_asig_est_id}", response_model=Meva_doc_asig_est)
async def obtener_eva_doc_asig_est(eva_doc_asig_est_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_eva_doc_asig_est.obtener_eva_doc_asig_est(eva_doc_asig_est_id)
    return rpta


@router.get("/obtener_eva_doc_asig_ests/", response_model=List[Meva_doc_asig_est])
async def obtener_eva_doc_asig_ests(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_eva_doc_asig_est.obtener_eva_doc_asig_ests()
    return rpta


@router.put("/actualizar_eva_doc_asig_est/")
async def actualizar_eva_doc_asig_est(eva_doc_asig_est: Meva_doc_asig_est, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_eva_doc_asig_est.actualizar_eva_doc_asig_est(eva_doc_asig_est)
    return rpta