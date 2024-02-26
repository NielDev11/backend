from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mevaluacionadmon import Mevaluacionadmon
from fastapi.encoders import jsonable_encoder


class Cevaluacionadmon:
    def crear_evaluacionadmon(self, evaluacionadmon: Mevaluacionadmon):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO evaluacionadmon (idtrabajador, idjefe, idcargo, fecha, periodo, idtipoevaluacion) VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    evaluacionadmon.idtrabajador,
                    evaluacionadmon.idjefe,
                    evaluacionadmon.idcargo,
                    evaluacionadmon.fecha,
                    evaluacionadmon.periodo,
                    evaluacionadmon.idtipoevaluacion,
                ),
            )
            conn.commit()
            return {"resultado": "evaluacionadmon creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_evaluacionadmon(self, evaluacionadmon_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from evaluacionadmon  WHERE id = %s", (evaluacionadmon_id,)
            )
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "idtrabajador": int(result[1]),
                "idjefe": int(result[2]),
                "idcargo": int(result[3]),
                "fecha": result[4],
                "periodo": result[5],
                "idtipoevaluacion": int(result[6]),
            }
            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="evaluacionadmon not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_evaluacionadmons(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from evaluacionadmon ")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    "id": data[0],
                    "idtrabajador": data[1],
                    "idjefe": data[2],
                    "idcargo": data[3],
                    "fecha": data[4],
                    "periodo": data[5],
                    "idtipoevaluacion": data[6],
                }
                payload.append(content)
            content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="evaluacionadmon not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def actualizar_evaluacionadmon(self, evaluacionadmon: Mevaluacionadmon):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            id = evaluacionadmon.id
            idtrabajador = evaluacionadmon.idtrabajador
            idjefe = evaluacionadmon.idjefe
            idcargo = evaluacionadmon.idcargo
            fecha = evaluacionadmon.fecha
            periodo = evaluacionadmon.periodo
            idtipoevaluacion = evaluacionadmon.idtipoevaluacion
            cursor.execute(
                """
                UPDATE evaluacionadmon
                SET 
                id = %s,
                idtrabajador = %s,
                idjefe = %s,
                idcargo = %s,
                fecha= %s,
                periodo = %s,
                idtipoevaluacion = %s
                WHERE id = %s
                """,
                (
                    idtrabajador,
                    idjefe,
                    idcargo,
                    fecha,
                    periodo,
                    idtipoevaluacion,
                    id
                ),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "evaluacionadmon actualizado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )