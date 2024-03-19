
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mgrupo_asignatura import Mgrupo_asignatura
from fastapi.encoders import jsonable_encoder
from controllers.cglobal import ControllerGlobal

class Cgrupo_asignatura:
    def __init__(self):
        self.cGlobal = ControllerGlobal("grupo_asignatura")
        
    def crear_grupo_asignatura(self, grupo_asignatura:  Mgrupo_asignatura ):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO grupo_asignatura (id_programa,id_asignatura,creditos,descripcion) VALUES (%s,%s,%s,%s)", (grupo_asignatura.id_programa,grupo_asignatura.id_asignatura,grupo_asignatura.creditos,grupo_asignatura.descripcion))
            conn.commit()            
            return {"resultado": "modelo creado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al crear el item: {str(e)}")
        
    def obtener_grupo_asignatura(self, grupo_asignatura_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT g.id, p.nombre as 'nombre_programa', a.nombre as 'nombre_asignatura', g.creditos, g.descripcion, g.estado FROM grupo_asignatura g INNER JOIN programa p ON g.id_programa = p.id INNER JOIN asignatura a ON g.id_asignatura = a.id WHERE g.id = %s ORDER BY g.estado DESC, g.id ASC", (grupo_asignatura_id,))
            result = cursor.fetchone()
            content = {} 
            content={
                    'id':int(result[0]),
                    'id_programa':result[1],
                    'id_asignatura':result[2],
                    'creditos':result[3],
                    'descripcion':result[4],
                    'estado':result[5]
            }
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found")  
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
       
    def obtener_grupo_asignaturas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT g.id, p.nombre as 'nombre_programa', a.nombre as 'nombre_asignatura', g.creditos, g.descripcion, g.estado FROM grupo_asignatura g INNER JOIN programa p ON g.id_programa = p.id INNER JOIN asignatura a ON g.id_asignatura = a.id ORDER BY g.estado DESC, g.id ASC;")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'programa':data[1],
                    'asignatura':data[2],
                    'creditos':data[3],
                    'descripcion':data[4],
                    'estado':data[5]
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
    
    
    def actualizar_grupo_asignatura(self,grupo_asignatura:  Mgrupo_asignatura ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                id = grupo_asignatura.id  
                id_programa = grupo_asignatura.id_programa
                id_asignatura = grupo_asignatura.id_asignatura
                creditos = grupo_asignatura.creditos   
                descripcion = grupo_asignatura.descripcion   
                cursor.execute("""
                UPDATE grupo_asignatura
                SET 
                id_programa = %s,
                id_asignatura = %s,
                creditos = %s,
                descripcion = %s
                WHERE id = %s
                """, (id_programa, id_asignatura, creditos,descripcion, id))
                conn.commit()
                cursor.close()
                return {"informacion":"Grupo asignatura actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        
    def deshabilitar_grupo_asignatura(self, grupo_asignatura_id: int):
        res = self.cGlobal.modificar_estado(grupo_asignatura_id,0)
        return res
                                                                                                                        
    def activar_grupo_asignatura(self, grupo_asignatura_id: int):
        res = self.cGlobal.modificar_estado(grupo_asignatura_id,1)
        return res
