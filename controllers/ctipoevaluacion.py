
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mtipoevaluacion import Mtipoevaluacion
from fastapi.encoders import jsonable_encoder
from controllers.cglobal import ControllerGlobal

class Ctipoevaluacion:
    def __init__(self):
        self.cGlobal = ControllerGlobal("tipoevaluacion")
    def crear_tipoevaluacion(self, tipoevaluacion:  Mtipoevaluacion ):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tipoevaluacion (nombre,descripcion) VALUES (%s, %s)", (tipoevaluacion.nombre,tipoevaluacion.descripcion))
            conn.commit()        
            cursor.close()
            return {"resultado": "modelo creado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        

    def obtener_tipoevaluacion(self, tipoevaluacion_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from tipoevaluacion  WHERE id = %s", (tipoevaluacion_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'descripcion':result[2],
                    'estado':result[3]
            }
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found")  
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")

       
    def obtener_tipoevaluacions(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from tipoevaluacion ORDER BY estado desc, id ASC")
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
    
    
    def actualizar_tipoevaluacion(self,tipoevaluacion:  Mtipoevaluacion ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                id=tipoevaluacion.id  
                nombre = tipoevaluacion.nombre
                descripcion = tipoevaluacion.descripcion   
                cursor.execute("""
                UPDATE tipoevaluacion
                SET 
                nombre = %s,
                descripcion = %s
                WHERE id = %s
                """, (nombre, descripcion, id))
                conn.commit()
                cursor.close()
                return {"informacion":"tipoevaluacion actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        
    def deshabilitar_tipoevaluacion(self, tipoevaluacion_id: int):
        res = self.cGlobal.modificar_estado(tipoevaluacion_id,0)
        return res
                                                                                                                        
    def activar_tipoevaluacion(self, tipoevaluacion_id: int):
        res = self.cGlobal.modificar_estado(tipoevaluacion_id,1)
        return res
    