
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.matributo import Matributo
from fastapi.encoders import jsonable_encoder
from controllers.cglobal import ControllerGlobal

class Catributo:
    def __init__(self):
        self.cGlobal = ControllerGlobal("atributo")
        
    def crear_atributo(self, atributo:  Matributo ):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO atributo (nombre,descripcion) VALUES (%s, %s)", (atributo.nombre,atributo.descripcion))
            conn.commit()            
            return {"resultado": "modelo creado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        

    def obtener_atributo(self, atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from atributo  WHERE id = %s", (atributo_id,))
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

       
    def obtener_atributos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from atributo ")
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
    
    
    def actualizar_atributo(self,atributo:  Matributo ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                id=atributo.id  
                nombre = atributo.nombre
                descripcion = atributo.descripcion   
                cursor.execute("""
                UPDATE atributo
                SET 
                nombre = %s,
                descripcion = %s
                WHERE id = %s
                """, (nombre, descripcion, id))
                conn.commit()
                cursor.close()
                return {"informacion":"atributo actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        
    def deshabilitar_atributo(self, atributo_id: int):
        res = self.cGlobal.modificar_estado(atributo_id,0)
        return res
                                                                                                                        
    def activar_atributo(self, atributo_id: int):
        res = self.cGlobal.modificar_estado(atributo_id,1)
        return res

    