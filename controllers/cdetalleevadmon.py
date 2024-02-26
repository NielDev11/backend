from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mdetalleevadmon import Mdetalleevadmon
from fastapi.encoders import jsonable_encoder


class Cdetalleevadmon:
    def crear_detalleevadmon(self, detalleevadmon: Mdetalleevadmon):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO detalleevadmon (idevaluacionadmon,idbancopregunta,calificacion) VALUES (%s, %s, %s)",
                (
                    detalleevadmon.idevaluacionadmon,
                    detalleevadmon.idbancopregunta,
                    detalleevadmon.calificacion,
                ),
            )
            conn.commit()
            return {"resultado": "detalleevadmon creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_detalleevadmon(self, detalleevadmon_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from detalleevadmon  WHERE id = %s", (detalleevadmon_id,)
            )
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "idevaluacionadmon": int(result[2]),
                "idbancopregunta": int(result[3]),
                "calificacion": float(result[3]),
            }
            ##payload.append(content)
            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="detalleevadmon not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_detalleevadmons(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from detalleevadmon ")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    "id": data[0],
                    "idevaluacionadmon": data[1],
                    "idbancopregunta": data[2],
                    "calificacion": data[3],
                }
                payload.append(content)
            content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="detalleevadmon not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def actualizar_detalleevadmon(self, detalleevadmon: Mdetalleevadmon):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            id = detalleevadmon.id
            idevaluacionadmon = detalleevadmon.idevaluacionadmon
            idbancopregunta = detalleevadmon.idbancopregunta
            calificacion = detalleevadmon.calificacion
            cursor.execute(
                """
                UPDATE detalleevadmon
                SET 
                idevaluacionadmon = %s,
                idbancopregunta = %s,
                calificacion = %s
                WHERE id = %s
                """,
                (idevaluacionadmon, idbancopregunta, calificacion, id),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "detalleevadmon actualizado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )


##user_controller = UserController()
