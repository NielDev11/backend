from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mcompetencia import Mcompetencia
from fastapi.encoders import jsonable_encoder
from controllers.cglobal import ControllerGlobal


class Ccompetencia:
    def __init__(self):
        self.cGlobal = ControllerGlobal("competencia")
    def crear_competencia(self, competencia: Mcompetencia):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO competencia (nombre,descripcion) VALUES (%s, %s)",
                (competencia.nombre, competencia.descripcion),
            )
            conn.commit()
            cursor.close()
            return {"resultado": "competencia creado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_competencia(self, competencia_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from competencia  WHERE id = %s ORDER BY estado desc, id ASC", (competencia_id,)
            )
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "nombre": result[1],
                "descripcion": result[2],
                "estado": result[3],
            }
            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_competencias(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from competencia ORDER BY estado desc, id ASC")
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
                raise HTTPException(status_code=404, detail="Model not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )
            
    def obtener_competencias_activos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from competencia WHERE estado = 1 ORDER BY estado DESC, id ASC"
            )
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
                raise HTTPException(status_code=404, detail="Competencia not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def actualizar_competencia(self, competencia: Mcompetencia):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            id = competencia.id
            nombre = competencia.nombre
            descripcion = competencia.descripcion
            cursor.execute(
                """
                UPDATE competencia
                SET 
                nombre = %s,
                descripcion = %s
                WHERE id = %s
                """,
                (nombre, descripcion, id),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "competencia actualizado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def deshabilitar_competencia(self, competencia_id: int):
        res = self.cGlobal.modificar_estado(competencia_id,0)
        return res
    
    def activar_competencia(self, competencia_id: int):
        res = self.cGlobal.modificar_estado(competencia_id,1)
        return res

