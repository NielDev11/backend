
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mevaluaciondoc import Mevaluaciondoc
from fastapi.encoders import jsonable_encoder

class Cevaluaciondoc:
    def crear_evaluaciondoc(self, evaluaciondoc:  Mevaluaciondoc ):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO evaluaciondoc (iddocente,periodo,idtipoevaluacion) VALUES (%s, %s, %s)", (evaluaciondoc.iddocente,evaluaciondoc.periodo,evaluaciondoc.idtipoevaluacion))
            conn.commit()            
            return {"resultado": "modelo creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        

    def obtener_evaluaciondoc(self, evaluaciondoc_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from evaluaciondoc  WHERE id = %s", (evaluaciondoc_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            content={
                    'id':int(result[0]),
                    'iddocente':int(result[1]),
                    'periodo':result[2],
                    'idtipoevaluacion':int(result[3])
            }
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found")  
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")

       
    def obtener_evaluaciondocs(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from evaluaciondoc ")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'iddocente':data[1],
                    'periodo':data[2],
                    'idtipoevaluacion':data[3]
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
    
    
    def actualizar_evaluaciondoc(self,evaluaciondoc:  Mevaluaciondoc ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                id=evaluaciondoc.id  
                iddocente = evaluaciondoc.iddocente
                periodo = evaluaciondoc.periodo   
                idtipoevaluacion = evaluaciondoc.idtipoevaluacion  
                cursor.execute("""
                UPDATE evaluaciondoc
                SET 
                iddocente = %s,
                periodo = %s,
                idtipoevaluacion = %s
                WHERE id = %s
                """, (iddocente, periodo, idtipoevaluacion, id))
                conn.commit()
                cursor.close()
                return {"informacion":"evaluaciondoc actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
    
       