from pydantic import BaseModel

class Mperfil(BaseModel):
    id: int = None
    nombre: str
    descripcion: str
    estado: int = None
   