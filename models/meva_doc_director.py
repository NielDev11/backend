from pydantic import BaseModel


class Meva_doc_director(BaseModel):
    id: int = None
    idejefe: int
    fecha: str
    idevaluaciondoc: int