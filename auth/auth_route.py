from fastapi import Header, HTTPException
from controllers.cuser import Login

login = Login()

def protected_route(Authorization: str = Header(...)):
    estado = login.separa_token(Authorization)
    if isinstance(estado, dict):
        return estado
    else:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
