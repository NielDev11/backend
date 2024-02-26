from pydantic import BaseModel

class Muser(BaseModel):
    usuario: str
    contrasena: str