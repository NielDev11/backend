from fastapi import HTTPException, Header
from models.muser import Muser
from datetime import datetime, timedelta
import jwt
from fastapi.responses import JSONResponse
from config.jw_confing import jwtConfing
from config.db_config import get_db_connection


class Login:   
    def create_access_token(self,data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=jwtConfing.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, jwtConfing.SECRET_KEY, algorithm=jwtConfing.ALGORITHM)
        return encoded_jwt

    def separa_token(self, token):
        if token is None:
            raise HTTPException(status_code=400, detail="Authorization header is missing")
        parts = token.split(" ")
        if len(parts) != 2 or parts[0].lower() != "bearer":
            raise HTTPException(status_code=400, detail="Invalid Authorization header format")
        token = parts[1]
        return self.validate_token(token, output=True)

    def validate_token(self, token, output=False): 
        try:
            if output:
                #print(token)
                return jwt.decode(token,jwtConfing.SECRET_KEY, algorithms=jwtConfing.ALGORITHM)
        except jwt.exceptions.DecodeError:
            return JSONResponse(content={"mesagge":"Invalido"},status_code=401)
        except jwt.exceptions.ExpiredSignatureError:
            return JSONResponse(content={"mesagge":"Expirado"},status_code=401)

    
    def verifytoken(self, Authorization: str = Header(None)):
        return self.separa_token(Authorization)
    
    def autenticacion(self, user: Muser):
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT id, usuario, contrasena, nombres, apellido1, telefono, idperfil, estado FROM usuario WHERE usuario = %s", (user.usuario,))
            user_data = cur.fetchone()
            cur.close()

            if user_data is not None:
                user_id, stored_usuario, stored_contrasena, stored_nombre, stored_apellido1, stored_telefono ,stored_idperfil, stored_estado = user_data

                if stored_estado == 1:
                    if user.contrasena == stored_contrasena:
                        token_data = {
                            "sub": stored_usuario,
                            "user_id": user_id,
                            "nombre": stored_nombre,
                            "apellido": stored_apellido1,
                            "telefono": stored_telefono,
                            "perfil": stored_idperfil
                        }
                        return {"access_token": self.create_access_token(data=token_data), **token_data}
                    else:
                        return {"message": "Usuario o contraseña incorrecta"}
                else:
                        return {"message": "Este usuario ya no se encuentra en la base de datos, por favor inicie sesion con una cuenta registrada"}
            else:
                return {"message": "Por favor ingrese su usuario y contraseña"}
        except Exception as e:
            print(e)
            return None

    # def autenticacion(self, user: Muser):
    #     try:
    #         conn = get_db_connection()
    #         cur = conn.cursor()            
    #         cur.execute("SELECT usuario, contrasena FROM usuario WHERE usuario = %s", (user.usuario,))
    #         user_data = cur.fetchone()
    #         cur.close()

    #         if user_data is not None:
    #             stored_usuario, stored_contrasena = user_data
    #             if user.contrasena == stored_contrasena:
    #                 return {"access_token": self.create_access_token(data={"sub": stored_usuario})}
    #             else:
    #                 return {"message": "Usuario o contraseña incorrecta"}
    #         else:
    #             return {"message": "Por favor ingrese su usuario y contraseña"}
    #         #return None, None  
    #     except Exception as e:
    #         print(e)
    #         return None, None  

