from persistance.db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
from enums.value_permission import ValuePermission
from enums.profile import Profile
import pymysql
from flask_login import UserMixin

class User(UserMixin):
    
    def __init__(self,id:int, name:str, email:str, password:str, profile:Profile, permissions:list[ValuePermission], is_active:bool):
        
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.profile = profile
        self.permissions = permissions
        self.is_active = is_active
         
    
    def check_email_exists(email) -> bool:
        """
            Verifica si la cuenta de correo electrónico ya se encuentra registrada.

            Parameters:
                email (str): Correo electrónico a validar.

            Returns:
                bool: True si el correo ya se encunetra registrado; de lo contrario, False.
        """
        connection = get_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT email from users WHERE email = %s"
        cursor.execute(sql, (email,))

        row = cursor.fetchone()

        cursor.close()
        connection.close()
        return row is not None
    
        
    def save(name: str, email:str, password:str) -> bool:
        """
            Guarda un registro de usuario en la base de datos

            Parameters:
                name (str): Nombre del usuario.
                email (str): Correo electrónico del usuario.
                password (str): Contraseña del usuario en texto plano.

            Returns:
                bool: True si la cuenta se guardó correctamente; de lo contrario, False.
        """
        try:
            connection = get_connection()
            cursor = connection.cursor()
            hash_password = generate_password_hash(password)

            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, hash_password))
            connection.commit()

            cursor.close()
            connection.close()
            return True
        except Exception as ex:
            print(f"Error saving users:{ex}")
            return False
    
    
    #probar con join
    def check_login(email:str, password:str):
        
        try:
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)

            query = "SELECT u.id, u.name, u.email, u.password, u.profile, u.is_active FROM users u JOIN permissions p ON u.id = p.user_id WHERE email = %s"
            cursor.execute(query, email)
            
            rs = cursor.fetchall()
            
            permissions = [ValuePermission(row['value']) for row in rs]
            
            user = cursor.fetchone()


            cursor.close()
            connection.close()
            
            if user and check_password_hash(user['password'], password):
                
                return User(user['id'],user['name'],user['email'],"", user['is_active'])
            
            return None
                
        except Exception as ex:
            print(f"Error loging user:{ex}")
            return False


    def get_by_id(user_id):
        try:
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)

            query = "SELECT id, name, email, password, profile, is_active FROM users WHERE id = %s"
            cursor.execute(query, user_id)
            
            user = cursor.fetchone()


            cursor.close()
            connection.close()
            
            if user:
                return User(user['id'],
                            user['name'],
                            user['email'], 
                            '', 
                            user['profile'],
                            user['is_active'])
                
        except Exception as ex:
            print(f"Error loging user:{ex}")
            return False
        
    
    