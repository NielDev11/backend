from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mnivel import Mnivel
from fastapi.encoders import jsonable_encoder
from controllers.cglobal import ControllerGlobal

class Cnivel:
    def __init__(self):
        self.cGlobal = ControllerGlobal("nivel")

    def crear_nivel(self, nivel: Mnivel):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO nivel (nombre,descripcion) VALUES (%s, %s)",
                (nivel.nombre, nivel.descripcion),
            )
            conn.commit()
            cursor.close()
            return {"resultado": "nivel creado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_nivel(self, nivel_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from nivel  WHERE id = %s", (nivel_id,))
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "nombre": result[1],
                "descripcion": result[2],
                "estado": result[3]
            }
            ##payload.append(content)
            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Nivel not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_niveles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from nivel ORDER BY estado desc, id ASC")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {"id": data[0], "nombre": data[1], "descripcion": data[2], "estado": data[3]}
                payload.append(content)
            content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Nivel not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )
        
    def obtener_niveles_activos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from nivel WHERE estado = 1 ORDER BY estado DESC, id ASC")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {"id": data[0], "nombre": data[1]}
                payload.append(content)
            content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Nivel not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def actualizar_nivel(self, nivel: Mnivel):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            id = nivel.id
            nombre = nivel.nombre
            descripcion = nivel.descripcion
            cursor.execute(
                """
                UPDATE nivel
                SET 
                nombre = %s,
                descripcion = %s
                WHERE id = %s
                """,
                (nombre, descripcion, id),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "nivel actualizado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def deshabilitar_nivel(self, nivel_id: int):
        res = self.cGlobal.modificar_estado(nivel_id,0)
        return res
                                                                                                                        
    def activar_nivel(self, nivel_id: int):
        res = self.cGlobal.modificar_estado(nivel_id,1)
        return res

