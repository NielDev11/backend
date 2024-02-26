
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mdetalle_evadoc_director import Mdetalle_evadoc_director
from fastapi.encoders import jsonable_encoder

class Cdetalle_evadoc_director:
    def crear_detalle_evadoc_director(self, detalle_evadoc_director:  Mdetalle_evadoc_director ):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO detalle_evadoc_director (ideva_doc_director,idbancopregunta,calificacion) VALUES (%s, %s, %s)", (detalle_evadoc_director.ideva_doc_director,detalle_evadoc_director.idbancopregunta,detalle_evadoc_director.calificacion))
            conn.commit()            
            return {"resultado": "modelo creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        

    def obtener_detalle_evadoc_director(self, detalle_evadoc_director_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from detalle_evadoc_director  WHERE id = %s", (detalle_evadoc_director_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            content={
                    'id':int(result[0]),
                    'ideva_doc_director':int(result[1]),
                    'idbancopregunta':int(result[2]),
                    'calificacion':float(result[3])
            }
            ##payload.append(content)            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found")  
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")

       
    def obtener_detalle_evadoc_directors(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from detalle_evadoc_director ")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'ideva_doc_director':data[1],
                    'idbancopregunta':data[2],
                    'calificacion':data[3]
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
    
    
    def actualizar_detalle_evadoc_director(self,detalle_evadoc_director:  Mdetalle_evadoc_director ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                id=detalle_evadoc_director.id  
                ideva_doc_director = detalle_evadoc_director.ideva_doc_director
                idbancopregunta = detalle_evadoc_director.idbancopregunta   
                calificacion = detalle_evadoc_director.calificacion   
                cursor.execute("""
                UPDATE detalle_evadoc_director
                SET 
                ideva_doc_director = %s,
                idbancopregunta = %s,
                calificacion = %s
                WHERE id = %s
                """, (ideva_doc_director, idbancopregunta, calificacion, id))
                conn.commit()
                cursor.close()
                return {"informacion":"detalle_evadoc_director actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
    