
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.masignatura import Masignatura
from fastapi.encoders import jsonable_encoder

class Casignatura:
    def crear_asignatura(self, asignatura:  Masignatura ):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO asignatura (nombre,codigo,descripcion,idprograma) VALUES (%s,%s,%s,%s)", (asignatura.nombre,asignatura.codigo,asignatura.descripcion,asignatura.idprograma))
            conn.commit()            
            return {"resultado": "modelo creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        

    def obtener_asignatura(self, asignatura_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from asignatura  WHERE id = %s", (asignatura_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'codigo':result[2],
                    'descripcion':result[3],
                    'idprograma':result[4]

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
            cursor.execute("SELECT * from asignatura ")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'codigo':data[2],
                    'descripcion':data[3],
                    'idprograma':data[4]
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
                id=asignatura.id  
                nombre = asignatura.nombre
                codigo = asignatura.codigo
                descripcion = asignatura.descripcion   
                idprograma = asignatura.idprograma  
                cursor.execute("""
                UPDATE asignatura
                SET 
                nombre = %s,
                codigo = %s,
                descripcion = %s,
                idprograma = %s
                WHERE id = %s
                """, (nombre, codigo, descripcion, idprograma, id))
                conn.commit()
                cursor.close()
                return {"informacion":"asignatura actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
    
       