from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mcomportamiento import Mcomportamiento
from fastapi.encoders import jsonable_encoder


class Ccomportamiento:
    def crear_comportamiento(self, comportamiento: Mcomportamiento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO comportamiento (nombre,descripcion,idcompetencia) VALUES (%s, %s, %s)",
                (
                    comportamiento.nombre,
                    comportamiento.descripcion,
                    comportamiento.idcompetencia,
                ),
            )
            conn.commit()
            return {"resultado": "comportamiento creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_comportamiento(self, comportamiento_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from comportamiento  WHERE id = %s", (comportamiento_id,)
            )
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "nombre": result[1],
                "descripcion": result[2],
                "idcompetencia": int(result[3]),
            }
            ##payload.append(content)
            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="comportamiento not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_comportamientos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from comportamiento ")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    "id": data[0],
                    "nombre": data[1],
                    "descripcion": data[2],
                    "idcompetencia": data[3],
                }
                payload.append(content)
            content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="comportamiento not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def actualizar_comportamiento(self, comportamiento: Mcomportamiento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            id = comportamiento.id
            nombre = comportamiento.nombre
            descripcion = comportamiento.descripcion
            idcompetencia = comportamiento.idcompetencia
            cursor.execute(
                """
                UPDATE comportamiento
                SET 
                nombre = %s,
                descripcion = %s,
                idcompetencia = %s
                WHERE id = %s
                """,
                (nombre, descripcion, idcompetencia, id),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "comportamiento actualizado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )


##user_controller = UserController()
