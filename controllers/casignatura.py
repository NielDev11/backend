
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.masignatura import Masignatura
from fastapi.encoders import jsonable_encoder
from controllers.cglobal import ControllerGlobal

class Casignatura:
    def __init__(self) -> None:
        self.cGlobal = ControllerGlobal("asignatura")
    def crear_asignatura(self, asignatura:  Masignatura ):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO asignatura (nombre,codigo,descripcion) VALUES (%s,%s,%s)", (asignatura.nombre,asignatura.codigo,asignatura.descripcion))
            conn.commit()            
            return {"resultado": "modelo creado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        

    def obtener_asignatura(self, asignatura_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from asignatura  WHERE id = %s", (asignatura_id,))
            result = cursor.fetchone()
            content = {} 
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'codigo':result[2],
                    'descripcion':result[3],
                    'estado':result[4]

            }
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found")  
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")

       
    def obtener_asignaturas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from asignatura order by estado desc, id ASC")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'codigo':data[2],
                    'descripcion':data[3],
                    'estado':data[4]
                }
                payload.append(content)     
            content = {}       
            json_data = jsonable_encoder(payload)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found")  
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
    
    
    def actualizar_asignatura(self,asignatura:  Masignatura ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                id = asignatura.id  
                nombre = asignatura.nombre
                codigo = asignatura.codigo
                descripcion = asignatura.descripcion   
                cursor.execute("""
                UPDATE asignatura
                SET 
                nombre = %s,
                codigo = %s,
                descripcion = %s
                WHERE id = %s
                """, (nombre, codigo, descripcion, id))
                conn.commit()
                cursor.close()
                return {"informacion":"asignatura actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        
    def deshabilitar_asignatura(self, asignatura_id: int ):
        res = self.cGlobal.modificar_estado(asignatura_id,0)
        return res
        
    def activar_asignatura(self, asignatura_id: int ):
        res = self.cGlobal.modificar_estado(asignatura_id,1)
        return res
