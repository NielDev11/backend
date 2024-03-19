from pydantic import BaseModel


class Mcomportamiento(BaseModel):
    id: int = None
    nombre: str
    descripcion: str
    idcompetencia: int
    estado: int = None
