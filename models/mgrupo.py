from pydantic import BaseModel

class Mgrupo(BaseModel):
    id: int = None
    nombre: str
    descripcion: str
    idasignatura: int