from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mgrupo import Mgrupo
from fastapi.encoders import jsonable_encoder


class Cgrupo:
    def crear_grupo(self, grupo: Mgrupo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO grupo (nombre,descripcion,idasignatura) VALUES (%s, %s, %s)",
                (grupo.nombre, grupo.descripcion, grupo.idasignatura),
            )
            conn.commit()
            return {"resultado": "grupo creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_grupo(self, grupo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from grupo  WHERE id = %s", (grupo_id,))
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "nombre": result[1],
                "descripcion": result[2],
                "idasignatura": int(result[3]),
            }
            ##payload.append(content)
            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="grupo not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_grupos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from grupo ")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    "id": data[0],
                    "nombre": data[1],
                    "descripcion": data[2],
                    "idasignatura": data[3],
                }
                payload.append(content)
            content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="grupo not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def actualizar_grupo(self, grupo: Mgrupo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            id = grupo.id
            nombre = grupo.nombre
            descripcion = grupo.descripcion
            idasignatura = grupo.idasignatura
            cursor.execute(
                """
                UPDATE grupo
                SET 
                nombre = %s,
                descripcion = %s,
                idasignatura = %s
                WHERE id = %s
                """,
                (nombre, descripcion, idasignatura, id),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "grupo actualizado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )
