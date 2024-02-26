from pydantic import BaseModel

class Mtipoevaluacion(BaseModel):
    id: int=None
    nombre: str
    descripcion: str
   