from fastapi import HTTPException
from config.db_config import get_db_connection

class ControllerGlobal:
    def __init__(self, nombre):
        self._nombre = nombre


class ControllerGlobal:
    def __init__(self, nombre_tabla):
        self._nombre_tabla = nombre_tabla

    # Esta funcion recive dos parametros, el primero id: que es el id del registro que se quiere eliminar
    # El segundo parametro es estado: Donde se indica si 1:quiere activar el registro o 0:desactivar el registro
    def modificar_estado(self, id: int, estado: int):
        try:
            # print("Nombre de la tabla: ", self._nombre_tabla)
            conn = get_db_connection()
            cursor = conn.cursor()
            query = f"UPDATE {self._nombre_tabla} SET estado = %s WHERE id = %s"
            cursor.execute(query, (estado, id))
            conn.commit()
            cursor.close()
            if estado == 1:
                return {"informacion": f"{self._nombre_tabla} activado con éxito"}
            else:
                return {"informacion": f"{self._nombre_tabla} deshabilitado con éxito"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al eliminar el item: {str(e)}")
