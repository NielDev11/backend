from pydantic import BaseModel


class Mdetalleevadoc(BaseModel):
    id: int = None
    ideva_doc_asig_est: int
    idbancopregunta: int
    calificacion: int
