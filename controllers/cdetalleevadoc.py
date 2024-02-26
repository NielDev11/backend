from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mdetalleevadoc import Mdetalleevadoc
from fastapi.encoders import jsonable_encoder


class Cdetalleevadoc:
    def crear_detalleevadoc(self, detalleevadoc: Mdetalleevadoc):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO detalleevadoc (ideva_doc_asig_est,idbancopregunta,calificacion) VALUES (%s, %s, %s)",
                (
                    detalleevadoc.ideva_doc_asig_est,
                    detalleevadoc.idbancopregunta,
                    detalleevadoc.calificacion,
                ),
            )
            conn.commit()
            return {"resultado": "detalleevadoc creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_detalleevadoc(self, detalleevadoc_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from detalleevadoc  WHERE id = %s", (detalleevadoc_id,)
            )
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "ideva_doc_asig_est": int(result[2]),
                "idbancopregunta": int(result[3]),
                "calificacion": int(result[3]),
            }
            ##payload.append(content)
            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="detalleevadoc not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_detalleevadocs(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from detalleevadoc ")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    "id": data[0],
                    "ideva_doc_asig_est": data[1],
                    "idbancopregunta": data[2],
                    "calificacion": data[3],
                }
                payload.append(content)
            content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="detalleevadoc not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def actualizar_detalleevadoc(self, detalleevadoc: Mdetalleevadoc):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            id = detalleevadoc.id
            ideva_doc_asig_est = detalleevadoc.ideva_doc_asig_est
            idbancopregunta = detalleevadoc.idbancopregunta
            calificacion = detalleevadoc.calificacion
            cursor.execute(
                """
                UPDATE detalleevadoc
                SET 
                ideva_doc_asig_est = %s,
                idbancopregunta = %s,
                calificacion = %s
                WHERE id = %s
                """,
                (ideva_doc_asig_est, idbancopregunta, calificacion, id),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "detalleevadoc actualizado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )


##user_controller = UserController()
