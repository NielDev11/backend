from pydantic import BaseModel


class Mnivel(BaseModel):
    id: int = None
    nombre: str
    descripcion: str
