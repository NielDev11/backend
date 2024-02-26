from pydantic import BaseModel

class Mdetalle_evadoc_director(BaseModel):
    id: int=None
    ideva_doc_director: int
    idbancopregunta: int
    calificacion: float
   