from pydantic import BaseModel


class Mevaluacionadmon(BaseModel):
    id: int = None
    idtrabajador: int
    idjefe: int
    idcargo: int
    fecha: str
    periodo: str
    idtipoevaluacion: int