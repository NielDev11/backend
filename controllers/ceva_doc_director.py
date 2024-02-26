from fastapi import HTTPException
from config.db_config import get_db_connection
from models.meva_doc_director import Meva_doc_director
from fastapi.encoders import jsonable_encoder


class Ceva_doc_director:
    def crear_eva_doc_director(self, eva_doc_director: Meva_doc_director):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO eva_doc_director (idejefe,fecha,idevaluaciondoc) VALUES (%s, %s, %s)",
                (
                    eva_doc_director.idejefe,
                    eva_doc_director.fecha,
                    eva_doc_director.idevaluaciondoc,
                ),
            )
            conn.commit()
            return {"resultado": "eva_doc_director creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_eva_doc_director(self, eva_doc_director_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from eva_doc_director  WHERE id = %s", (eva_doc_director_id,)
            )
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "idejefe": int(result[1]),
                "fecha": result[2],
                "idevaluaciondoc": int(result[3]),
            }
            ##payload.append(content)
            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="eva_doc_director not found"
                )
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_eva_doc_directors(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from eva_doc_director ")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    "id": data[0],
                    "idejefe": data[1],
                    "fecha": data[2],
                    "idevaluaciondoc": data[3],
                }
                payload.append(content)
            content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="eva_doc_director not found"
                )
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def actualizar_eva_doc_director(self, eva_doc_director: Meva_doc_director):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            id = eva_doc_director.id
            idejefe = eva_doc_director.idejefe
            fecha = eva_doc_director.fecha
            idevaluaciondoc = eva_doc_director.idevaluaciondoc
            cursor.execute(
                """
                UPDATE eva_doc_director
                SET 
                idejefe = %s,
                fecha = %s,
                idevaluaciondoc = %s
                WHERE id = %s
                """,
                (idejefe, fecha, idevaluaciondoc, id),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "eva_doc_director actualizado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )