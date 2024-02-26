from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mbancopregunta import Mbancopregunta
from fastapi.encoders import jsonable_encoder


class Cbancopregunta:
    def crear_bancopregunta(self, bancopregunta: Mbancopregunta):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO bancopregunta (idnivel,idcomportamiento,pregunta) VALUES (%s, %s, %s)",
                (
                    bancopregunta.idnivel,
                    bancopregunta.idcomportamiento,
                    bancopregunta.pregunta,
                ),
            )
            conn.commit()
            return {"resultado": "bancopregunta creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_bancopregunta(self, bancopregunta_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from bancopregunta  WHERE id = %s", (bancopregunta_id,)
            )
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "idnivel": int(result[1]),
                "idcomportamiento": int(result[2]),
                "pregunta": result[3],
            }
            ##payload.append(content)
            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="bancopregunta not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_bancopreguntas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from bancopregunta ")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    "id": data[0],
                    "idnivel": data[1],
                    "idcomportamiento": data[2],
                    "pregunta": data[3],
                }
                payload.append(content)
            content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="bancopregunta not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def actualizar_bancopregunta(self, bancopregunta: Mbancopregunta):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            id = bancopregunta.id
            idnivel = bancopregunta.idnivel
            idcomportamiento = bancopregunta.idcomportamiento
            pregunta = bancopregunta.pregunta
            cursor.execute(
                """
                UPDATE bancopregunta
                SET 
                idnivel = %s,
                idcomportamiento = %s,
                pregunta = %s
                WHERE id = %s
                """,
                (idnivel, idcomportamiento, pregunta, id),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "bancopregunta actualizado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )


##user_controller = UserController()
