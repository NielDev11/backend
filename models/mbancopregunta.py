from pydantic import BaseModel


class Mbancopregunta(BaseModel):
    id: int = None
    idnivel: int
    idcomportamiento: int
    pregunta: str
    estado: int = None

