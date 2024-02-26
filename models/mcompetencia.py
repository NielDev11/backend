from pydantic import BaseModel


class Mcompetencia(BaseModel):
    id: int = None
    nombre: str
    descripcion: str
