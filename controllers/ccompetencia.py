from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mcompetencia import Mcompetencia
from fastapi.encoders import jsonable_encoder


class Ccompetencia:
    def crear_competencia(self, competencia: Mcompetencia):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO competencia (nombre,descripcion) VALUES (%s, %s)",
                (competencia.nombre, competencia.descripcion),
            )
            conn.commit()
            return {"resultado": "competencia creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_competencia(self, competencia_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from competencia  WHERE id = %s", (competencia_id,)
            )
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "nombre": result[1],
                "descripcion": result[2],
            }
            ##payload.append(content)
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
            cursor.execute("SELECT * from competencia ")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {"id": data[0], "nombre": data[1], "descripcion": data[2]}
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


##user_controller = UserController()
