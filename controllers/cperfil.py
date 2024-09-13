
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.mperfil import Mperfil
from fastapi.encoders import jsonable_encoder
from controllers.cglobal import ControllerGlobal

class Cperfil:

    def __init__(self) -> None:
        self.activar_registro = 1
        self.deshabilitar_registro = 0
        self.nombre_tabla = "perfil"
        self.cGlobal = ControllerGlobal(self.nombre_tabla)

    def crear_perfil(self, perfil:  Mperfil ):   

        if not perfil.nombre.strip() or not perfil.descripcion.strip():
            raise HTTPException(status_code=400, detail="El nombre y la descripción son obligatorios")
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO perfil (nombre,descripcion) VALUES (%s, %s)", (perfil.nombre,perfil.descripcion))
            conn.commit()            
            return {"resultado": "perfil creado con exito"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        

    def obtener_perfil(self, perfil_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from perfil  WHERE id = %s", (perfil_id,))
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

       
    def obtener_perfiles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from perfil ORDER BY estado DESC, id ASC")
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
        
    def obtener_perfiles_activos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from perfil WHERE estado = 1 ORDER BY estado DESC, id ASC")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1]
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
    
    
    def actualizar_perfil(self,perfil:  Mperfil ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                id=perfil.id  
                nombre = perfil.nombre
                descripcion = perfil.descripcion   
                cursor.execute("""
                UPDATE perfil
                SET 
                nombre = %s,
                descripcion = %s
                WHERE id = %s
                """, (nombre, descripcion, id))
                conn.commit()
                cursor.close()
                return {"informacion":"perfil actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        
    def deshabilitar_perfil(self, perfil_id: int):
        res = self.cGlobal.modificar_estado(perfil_id,self.deshabilitar_registro)
        return res
    
    def activar_perfil(self, perfil_id: int):
        res = self.cGlobal.modificar_estado(perfil_id,self.activar_registro)
        return res
    