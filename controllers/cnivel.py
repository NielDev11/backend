from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mnivel import Mnivel
from fastapi.encoders import jsonable_encoder


class Cnivel:
    def crear_nivel(self, nivel: Mnivel):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO nivel (nombre,descripcion) VALUES (%s, %s)",
                (nivel.nombre, nivel.descripcion),
            )
            conn.commit()
            return {"resultado": "nivel creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_nivel(self, nivel_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from nivel  WHERE id = %s", (nivel_id,))
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
                raise HTTPException(status_code=404, detail="Nivel not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_niveles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from nivel ")
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
                raise HTTPException(status_code=404, detail="Nivel not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def actualizar_nivel(self, nivel: Mnivel):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            id = nivel.id
            nombre = nivel.nombre
            descripcion = nivel.descripcion
            cursor.execute(
                """
                UPDATE nivel
                SET 
                nombre = %s,
                descripcion = %s
                WHERE id = %s
                """,
                (nombre, descripcion, id),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "nivel actualizado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )


##user_controller = UserController()
