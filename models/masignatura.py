from pydantic import BaseModel

class Masignatura(BaseModel):
    id: int=None
    nombre: str
    codigo: str
    descripcion: str
    idprograma: int
   