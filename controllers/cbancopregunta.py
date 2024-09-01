from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mbancopregunta import Mbancopregunta
from fastapi.encoders import jsonable_encoder
from controllers.cglobal import ControllerGlobal


class Cbancopregunta:

    def __init__(self) -> None:
        self.cGlobal = ControllerGlobal("bancopregunta")

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
            cursor.execute("SELECT b.id, b.idnivel, n.nombre as 'nombre_nivel', b.idcomportamiento ,c.nombre as 'nombre_comportamiento', b.pregunta, b.estado from bancopregunta b INNER JOIN nivel n ON b.idnivel = n.id INNER JOIN comportamiento c ON b.idcomportamiento = c.id ORDER BY b.estado DESC, b.id ASC")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    "id": data[0],
                    "idnivel": data[1],
                    "nombre_nivel": data[2],
                    "idcomportamiento": data[3],
                    "nombre_comportamiento": data[4],
                    "pregunta": data[5],
                    "estado": data[6]
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
        
    ##Se Filtran las preguntas por el nivel al que pertenecen
    def filtrar_bancopreguntas(self, bancopregunta_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
                SELECT b.id, b.idcomportamiento, c.nombre as nombre_comportamiento, b.pregunta
                FROM bancopregunta b
                INNER JOIN comportamiento c ON b.idcomportamiento = c.id
                WHERE b.idnivel = %s AND b.estado = 1
                ORDER BY b.idcomportamiento;
            """
            cursor.execute(query, (bancopregunta_id,))

            result = cursor.fetchall()
            payload = [
                {
                    "id": data[0],
                    "idcomportamiento": data[1],
                    "nombre_comportamiento": data[2],
                    "pregunta": data[3]
                }
                for data in result
            ]
            if result:
                return jsonable_encoder(payload)
            else:
                raise HTTPException(status_code=404, detail="bancopregunta not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al filtrar bancopreguntas: {str(e)}"
            )

        
    def max_bancopreguntas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(idcomportamiento) as 'max_bancopregunta' FROM bancopregunta WHERE idnivel = 2;")
            result = cursor.fetchone()  # Cambiado a fetchone() para obtener una sola fila

            if result:
                content = {
                    "max_bancopregunta": result[0]  # Crear un solo objeto
                }
                return jsonable_encoder(content)  # Devolver un único objeto en lugar de una lista
            else:
                raise HTTPException(status_code=404, detail="bancopregunta not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al obtener el max_bancopregunta: {str(e)}"
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

    def deshabilitar_bancopregunta(self, bancopregunta_id: int ):
        res = self.cGlobal.modificar_estado(bancopregunta_id,0)
        return res
        
    def activar_bancopregunta(self, bancopregunta_id: int ):
        res = self.cGlobal.modificar_estado(bancopregunta_id,1)
        return res
