
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.musuario import Musuario
from fastapi.encoders import jsonable_encoder

class Cusuario:
    def crear_usuario(self, usuario:  Musuario ):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuario (usuario,contrasena,nombres,apellido1,apellido2,tipodocumento,identificacion,telefono,idperfil) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (usuario.usuario,usuario.contrasena,usuario.nombres, usuario.apellido1, usuario.apellido2, usuario.tipodocumento, usuario.identificacion, usuario.telefono, usuario.idperfil))
            conn.commit()            
            return {"resultado": "Usuario creado"}
            cursor.close()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")
        

    def obtener_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from usuario  WHERE id = %s", (usuario_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            content={
                    'id':int(result[0]),
                    'usuario':result[1],
                    'contrasena':result[2],
                    'nombres':result[3],
                    'apellido1':result[4],
                    'apellido2':result[5],
                    'tipodocumento':result[6],
                    'identificacion':result[7],
                    'telefono':result[8],
                    'idperfil':result[9],
                    'estado':result[10]
            }
            json_data = jsonable_encoder(content) 
            if result:
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found") 

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al ver el item {str(e)}")

       
    def obtener_usuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            #cursor.execute("SELECT * from usuario WHERE estado = 1")
            cursor.execute("SELECT u.id, u.usuario, u.contrasena, u.nombres, u.apellido1, u.apellido2, u.tipodocumento, u.identificacion, u.telefono, p.nombre as 'nombre_perfil', u.estado from usuario as u join perfil as p on p.id = u.idperfil order by estado desc;")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'usuario':data[1],
                    'contrasena':data[2],
                    'nombres':data[3],
                    'apellido1':data[4],
                    'apellido2':data[5],
                    'tipodocumento':data[6],
                    'identificacion':data[7],
                    'telefono':data[8],
                    'idperfil':data[9],
                    'estado':data[10]

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

    def obtener_usuarios_eliminados(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from usuario WHERE estado = 0")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'usuario':data[1],
                    'contrasena':data[2],
                    'nombres':data[3],
                    'apellido1':data[4],
                    'apellido2':data[5],
                    'tipodocumento':data[6],
                    'identificacion':data[7],
                    'telefono':data[8],
                    'idperfil':data[9],
                    'estado':data[10]

                }
                payload.append(content)     
            content = {}       
            json_data = jsonable_encoder(payload)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Model not found")  
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al visualizar el item: {str(e)}")
    
    
    def actualizar_usuario(self,usuario:  Musuario ):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE usuario
                SET 
                usuario = %s,
                contrasena = %s,
                nombres = %s,
                apellido1 = %s,
                apellido2 = %s,
                tipodocumento = %s,
                identificacion = %s,
                telefono = %s,
                idperfil = %s,
                estado = %s
                WHERE id = %s
                """,
                (
                    usuario.usuario,
                    usuario.contrasena,
                    usuario.nombres,
                    usuario.apellido1,
                    usuario.apellido2,
                    usuario.tipodocumento,
                    usuario.identificacion,
                    usuario.telefono,
                    usuario.idperfil,
                    usuario.estado,
                    usuario.id,
                ),
            )
            conn.commit()
            cursor.close()
            return {"informacion": "usuario actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el item: {str(e)}")

    def eliminar_usuario(self, usuario_id: int ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                estado=0

                cursor.execute(""" 
                UPDATE usuario SET estado = %s WHERE id = %s
                """, (estado, usuario_id))
                conn.commit()
                cursor.close()
                return {"informacion":"Usuario eliminado con exito"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al eliminar el item: {str(e)}")
        
    def activar_usuario(self, usuario_id: int ):
        try:    
                conn = get_db_connection()
                cursor = conn.cursor()   
                estado=1

                cursor.execute(""" 
                UPDATE usuario SET estado = %s WHERE id = %s
                """, (estado, usuario_id))
                conn.commit()
                cursor.close()
                return {"informacion":"Usuario recuperado con exito"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al eliminar el item: {str(e)}")
