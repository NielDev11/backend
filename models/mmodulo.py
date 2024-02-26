from pydantic import BaseModel

class Mmodulo(BaseModel):
    id: int=None
    nombre: str
    descripcion: str
   