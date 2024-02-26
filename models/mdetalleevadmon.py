from pydantic import BaseModel


class Mdetalleevadmon(BaseModel):
    id: int = None
    idevaluacionadmon: int
    idbancopregunta: int
    calificacion: float
