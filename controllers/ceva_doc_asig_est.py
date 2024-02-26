from fastapi import HTTPException
from config.db_config import get_db_connection
from models.meva_doc_asig_est import Meva_doc_asig_est
from fastapi.encoders import jsonable_encoder


class Ceva_doc_asig_est:
    def crear_eva_doc_asig_est(self, eva_doc_asig_est: Meva_doc_asig_est):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO eva_doc_asig_est (idestudiante,idgrupo,fecha,idevaluaciondoc) VALUES (%s, %s, %s, %s)",
                (
                    eva_doc_asig_est.idestudiante,
                    eva_doc_asig_est.idgrupo,
                    eva_doc_asig_est.fecha,
                    eva_doc_asig_est.idevaluaciondoc,
                ),
            )
            conn.commit()
            return {"resultado": "eva_doc_asig_est creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_eva_doc_asig_est(self, eva_doc_asig_est_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from eva_doc_asig_est  WHERE id = %s", (eva_doc_asig_est_id,)
            )
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "idestudiante": int(result[1]),
                "idgrupo": int(result[2]),
                "fecha": result[3],
                "idevaluaciondoc": int(result[4])
            }
            ##payload.append(content)
            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="eva_doc_asig_est not found"
                )
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_eva_doc_asig_ests(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from eva_doc_asig_est ")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    "id": data[0],
                    "idestudiante": data[1],
                    "idgrupo": data[2],
                    "fecha": data[3],
                    "idevaluaciondoc": data[4],
                }
                payload.append(content)
            content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="eva_doc_asig_est not found"
                )
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def actualizar_eva_doc_asig_est(self, eva_doc_asig_est: Meva_doc_asig_est):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            id = eva_doc_asig_est.id
            idestudiante = eva_doc_asig_est.idestudiante
            idgrupo = eva_doc_asig_est.idgrupo
            fecha = eva_doc_asig_est.fecha
            idevaluaciondoc = eva_doc_asig_est.idevaluaciondoc
            cursor.execute(
                """
                UPDATE eva_doc_asig_est
                SET 
                idestudiante = %s,
                idgrupo = %s,
                fecha = %s,
                idevaluaciondoc = %s
                WHERE id = %s
                """,
                (idestudiante, idgrupo, fecha, idevaluaciondoc, id),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "eva_doc_asig_est actualizado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )