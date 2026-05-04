from enums.value_permission import ValuePermission
from persistance.db import get_connection

class Permission:
    def __init__(self, id: int, value: ValuePermission, id_user: int):
        self.id = id
        self.value = value
        self.id_user = id_user
        
    def get_permissions_by_user(user_id: int) -> list[ValuePermission]:
        
        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = "SELECT id, value, user_id FROM permissions WHERE user_id = %s"
            cursor.execute(query, user_id)
        except Exception as ex:
            print("Error trayendo al los permisos del usuario", ex)
        
        permissions = [ValuePermission(row[1]) for row in cursor.fetchall()] #row[1] es el value del permission

        cursor.close()
        connection.close()
        return permissions
            
    
    def edit_permissions_by_user(user_id: int, permissions: list[int]) -> bool:
        
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = "DELETE FROM permissions WHERE user_id = %s"
            
            cursor.execute(query, (user_id,))
            
            for p in permissions:
                cursor.execute(
                    "INSERT INTO permissions (value, user_id) VALUES (%s, %s)",
                    (p, user_id)
                )
            
            connection.commit()
        
            return True
        
        except Exception as ex:
            connection.rollback()
            print("Error actualizando permisos:", ex)
            return False
        finally:
            cursor.close()
            connection.close()