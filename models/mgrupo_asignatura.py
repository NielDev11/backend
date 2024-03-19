from pydantic import BaseModel

class Mgrupo_asignatura(BaseModel):
    id: int = None
    id_programa: int
    id_asignatura: int
    creditos: int
    descripcion: str
    estado: int = None

