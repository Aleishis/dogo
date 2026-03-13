from persistance.db import get_connection
from werkzeug.security import generate_password_hash

class User:
    
    def __init__(self, id:int, name:str, email:str, password:str):
        
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        
    def save(name:str, email:str, password:str): # type: ignore
        connection = get_connection()
        
        cursor = connection.cursor()
        
        hash_password = generate_password_hash(password)
        
        query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        
        cursor.execute(query, (name, email, hash_password))
        
        connection.commit()
        
        cursor.close()
        connection.close()