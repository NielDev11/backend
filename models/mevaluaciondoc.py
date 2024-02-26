from pydantic import BaseModel

class Mevaluaciondoc(BaseModel):
    id: int=None
    iddocente: int
    periodo: str
    idtipoevaluacion: int