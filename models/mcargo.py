from pydantic import BaseModel


class Mcargo(BaseModel):
    id: int = None
    nombre: str
    descripcion: str
    idnivel: int
    estado: int = None
