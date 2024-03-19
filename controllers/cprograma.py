
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mprograma import Mprograma
from fastapi.encoders import jsonable_encoder
from controllers.cglobal import ControllerGlobal

class Cprograma:

    def __init__(self) -> None:
        self.cGlobal = ControllerGlobal("programa")
        
    def crear_programa(self, programa:  Mprograma ):   	
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO programa (nombre,descripcion,idfacultad) VALUES (%s, %s, %s)", (programa.nombre,programa.descripcion,programa.idfacultad))
            conn.commit()         
            cursor.close()
            return {"resultado": "modelo creado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        

    def obtener_programa(self, programa_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT p.id, p.nombre, p.descripcion, f.nombre as 'nombre_facultad', p.estado FROM programa p INNER JOIN facultad f ON p.idfacultad = f.id WHERE p.id = %s ORDER BY estado DESC, p.id ASC", (programa_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'descripcion':result[2],
                    'idfacultad':result[3],
                    'estado':result[4]
            }
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found")  
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")

       
    def obtener_programas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT p.id, p.nombre, p.descripcion, f.nombre as 'nombre_facultad', p.estado FROM programa p INNER JOIN facultad f ON p.idfacultad = f.id ORDER BY estado DESC, p.id ASC")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'descripcion':data[2],
                    'idfacultad':data[3],
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
    
    
    def actualizar_programa(self,programa:  Mprograma ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                id=programa.id  
                nombre = programa.nombre
                descripcion = programa.descripcion   
                idfacultad = programa.idfacultad
                cursor.execute("""
                UPDATE programa
                SET 
                nombre = %s,
                descripcion = %s,
                idfacultad = %s
                WHERE id = %s
                """, (nombre, descripcion, idfacultad, id))
                conn.commit()
                cursor.close()
                return {"informacion":"programa actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        
    def deshabilitar_programa(self, programa_id: int):
        res = self.cGlobal.modificar_estado(programa_id,0)
        return res
    
    def activar_programa(self, programa_id: int):
        res = self.cGlobal.modificar_estado(programa_id,1)
        return res
    