
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mmoduloxperfil import Mmoduloxperfil
from fastapi.encoders import jsonable_encoder

class Cmoduloxperfil:
    def crear_moduloxperfil(self, moduloxperfil:  Mmoduloxperfil ):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO moduloxperfil (idmodulo,idperfil,descripcion) VALUES (%s,%s,%s)", (moduloxperfil.idmodulo,moduloxperfil.idperfil,moduloxperfil.descripcion))
            conn.commit()            
            return {"resultado": "modelo creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        

    def obtener_moduloxperfil(self, moduloxperfil_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from moduloxperfil  WHERE id = %s", (moduloxperfil_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            content={
                    'id':int(result[0]),
                    'idmodulo':result[1],
                    'idperfil':result[2],
                    'descripcion':result[3]
            }
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found")  
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")

       
    def obtener_moduloxperfils(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from moduloxperfil ")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'idmodulo':data[1],
                    'idperfil':data[2],
                    'descripcion':data[3]
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
    
    
    def actualizar_moduloxperfil(self,moduloxperfil:  Mmoduloxperfil ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                id=moduloxperfil.id  
                idmodulo = moduloxperfil.idmodulo
                idperfil = moduloxperfil.idperfil
                descripcion = moduloxperfil.descripcion   
                cursor.execute("""
                UPDATE moduloxperfil
                SET 
                idmodulo = %s,
                idperfil = %s,
                descripcion = %s
                WHERE id = %s
                """, (idmodulo, idperfil, descripcion, id))
                conn.commit()
                cursor.close()
                return {"informacion":"moduloxperfil actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
    
       