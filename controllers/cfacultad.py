
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mfacultad import Mfacultad
from fastapi.encoders import jsonable_encoder
from controllers.cglobal import ControllerGlobal

class Cfacultad:
    
    def __init__(self):
        self.cGlobal = ControllerGlobal("facultad")

    def crear_facultad(self, facultad:  Mfacultad ):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO facultad (nombre,descripcion) VALUES (%s, %s)", (facultad.nombre,facultad.descripcion))
            conn.commit()            
            cursor.close()
            return {"resultado": "modelo creado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        

    def obtener_facultad(self, facultad_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from facultad  WHERE id = %s", (facultad_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'descripcion':result[2],
                    'estado':result[3]
            }
            ##payload.append(content)            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found")  
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")

       
    def obtener_facultades(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from facultad ORDER BY estado desc, id ASC")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'descripcion':data[2],
                    'estado':data[3]
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
    
    
    def actualizar_facultad(self,facultad:  Mfacultad ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                id=facultad.id  
                nombre = facultad.nombre
                descripcion = facultad.descripcion   
                cursor.execute("""
                UPDATE facultad
                SET 
                nombre = %s,
                descripcion = %s
                WHERE id = %s
                """, (nombre, descripcion, id))
                conn.commit()
                cursor.close()
                return {"informacion":"facultad actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        
    def deshabilitar_facultad(self, facultad_id: int):
        res = self.cGlobal.modificar_estado(facultad_id,0)
        return res
    
    def activar_facultad(self, facultad_id: int):
        res = self.cGlobal.modificar_estado(facultad_id,1)
        return res

    