
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mmodulo import Mmodulo
from fastapi.encoders import jsonable_encoder

class Cmodulo:
    def crear_modulo(self, modulo:  Mmodulo ):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO modulo (nombre,descripcion) VALUES (%s, %s)", (modulo.nombre,modulo.descripcion))
            conn.commit()            
            return {"resultado": "modelo creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        

    def obtener_modulo(self, modulo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from modulo  WHERE id = %s", (modulo_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'descripcion':result[2]
            }
            ##payload.append(content)            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found")  
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")

       
    def obtener_modulos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from modulo ")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'descripcion':data[2]
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
    
    
    def actualizar_modulo(self,modulo:  Mmodulo ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                id=modulo.id  
                nombre = modulo.nombre
                descripcion = modulo.descripcion   
                cursor.execute("""
                UPDATE modulo
                SET 
                nombre = %s,
                descripcion = %s
                WHERE id = %s
                """, (nombre, descripcion, id))
                conn.commit()
                cursor.close()
                return {"informacion":"modulo actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
    
       

##user_controller = UserController()