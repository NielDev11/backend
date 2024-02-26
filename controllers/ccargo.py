from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mcargo import Mcargo
from fastapi.encoders import jsonable_encoder


class Ccargo:
    def crear_cargo(self, cargo: Mcargo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO cargo (nombre,descripcion,idnivel) VALUES (%s, %s, %s)",
                (cargo.nombre, cargo.descripcion, cargo.idnivel),
            )
            conn.commit()
            return {"resultado": "cargo creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_cargo(self, cargo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from cargo  WHERE id = %s", (cargo_id,))
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "nombre": result[1],
                "descripcion": result[2],
                "idnivel": int(result[3]),
            }
            ##payload.append(content)
            json_data = jsonable_encoder(content)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Cargo not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_cargos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from cargo ")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    "id": data[0],
                    "nombre": data[1],
                    "descripcion": data[2],
                    "idnivel": data[3],
                }
                payload.append(content)
            content = {}
            json_data = jsonable_encoder(payload)
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Cargo not found")
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def actualizar_cargo(self, cargo: Mcargo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            id = cargo.id
            nombre = cargo.nombre
            descripcion = cargo.descripcion
            idnivel = cargo.idnivel
            cursor.execute(
                """
                UPDATE cargo
                SET 
                nombre = %s,
                descripcion = %s,
                idnivel = %s
                WHERE id = %s
                """,
                (nombre, descripcion, idnivel, id),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "cargo actualizado"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )


##user_controller = UserController()
