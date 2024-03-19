from pydantic import BaseModel

class Mfacultad(BaseModel):
    id: int=None
    nombre: str
    descripcion: str
    estado: int = None