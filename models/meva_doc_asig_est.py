from pydantic import BaseModel

class Meva_doc_asig_est(BaseModel):
    id: int = None
    idestudiante: int
    idgrupo: int
    fecha: str
    idevaluaciondoc: int