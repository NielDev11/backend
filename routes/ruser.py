from fastapi import APIRouter, HTTPException, Header, requests
from controllers.cuser import Login
from models.muser import Muser
from typing import List

router = APIRouter()

login = Login()

# @router.post("/login")
# async def loginJwt(user: Muser):
#     token = login.autenticacion(user)
#     if token:
#         return {"access_token": token, "token_type": "bearer"}
#     else:
#         raise HTTPException(status_code=401, detail="Credenciales incorrectas")

# @router.post("/login")
# async def loginJwt(user: Muser):
#     response = login.autenticacion(user)
#     if "message" in response:
#         raise HTTPException(status_code=401, detail=response["message"])
#     else:
#         return {"access_token": response, "token_type": "bearer"}

@router.post("/login")
async def loginJwt(user: Muser):
    response = login.autenticacion(user)
    if response is None:
        raise HTTPException(status_code=500, detail="Error en la autenticación")

    if "message" in response:
        raise HTTPException(status_code=401, detail=response["message"])
    else:
        return response 

@router.post("/verifytoken")
async def verify(Authorization: str = Header(None)):
    rpta = login.verifytoken(Authorization)
    return rpta