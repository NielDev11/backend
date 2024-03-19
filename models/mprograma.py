from pydantic import BaseModel

class Mprograma(BaseModel):
    id: int=None
    nombre: str
    descripcion: str
    idfacultad: int
    estado: int = None
   