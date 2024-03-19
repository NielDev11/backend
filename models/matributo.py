from pydantic import BaseModel

class Matributo(BaseModel):
    id: int=None
    nombre: str
    descripcion: str
    estado: int = None
   