from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mcargo import Mcargo
from fastapi.encoders import jsonable_encoder
from controllers.cglobal import ControllerGlobal


class Ccargo:
    def __init__(self):
        self.activar_registro = 1
        self.deshabilitar_registro = 0
        self.nombre_tabla = "cargo"
        self.cGlobal = ControllerGlobal(self.nombre_tabla)

    def crear_cargo(self, cargo: Mcargo):
        if not all([cargo.nombre.strip(), cargo.descripcion.strip(), cargo.idnivel]):
            raise HTTPException(status_code=400, detail="Todos los campos son obligatorios")
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO cargo (nombre,descripcion,idnivel) VALUES (%s, %s, %s)",
                (cargo.nombre, cargo.descripcion, cargo.idnivel),
            )
            conn.commit()
            cursor.close()
            return {"resultado": "cargo creado con exito"}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al actualizar el item: {str(e)}"
            )

    def obtener_cargo(self, cargo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT c.id, c.nombre, c.descripcion, n.nombre as 'nombre_cargo', c.estado FROM cargo c INNER JOIN nivel n ON c.idnivel = n.id WHERE c.id = %s", (cargo_id,))
            result = cursor.fetchone()
            payload = []
            content = {}
            content = {
                "id": int(result[0]),
                "nombre": result[1],
                "descripcion": result[2],
                "idnivel": str(result[3]),
                "estado": int(result[4])
            }
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
            cursor.execute("SELECT c.id, c.nombre, c.descripcion, n.nombre as 'nombre_nivel', c.estado FROM cargo c INNER JOIN nivel n ON c.idnivel = n.id order by estado desc, c.id ASC")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    "id": data[0],
                    "nombre": data[1],
                    "descripcion": data[2],
                    "idnivel": data[3],
                    "estado": data[4]
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
        
    def deshabilitar_cargo(self, cargo_id: int):
        res = self.cGlobal.modificar_estado(cargo_id, self.deshabilitar_registro)
        return res
    
    def activar_cargo(self, cargo_id: int):
        res = self.cGlobal.modificar_estado(cargo_id, self.activar_registro)
        return res