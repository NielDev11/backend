from pydantic import BaseModel

class Musuario(BaseModel):
    id: int = None
    usuario: str
    contrasena: str
    nombres: str
    apellido1: str
    apellido2: str
    tipodocumento: str
    identificacion: str
    telefono: str
    idperfil: int
    estado: int = None