from persistance.db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
from enums.value_permission import ValuePermission
from enums.profile import Profile
import pymysql
from flask_login import UserMixin

connection = get_connection()
cursor = connection.cursor(pymysql.cursors.DictCursor)

query = "SELECT u.id, u.name, u.email, u.password, u.profile, u.is_active FROM users u JOIN permissions p ON u.id = p.user_id WHERE email = %s"
cursor.execute(query, "alexi")
            
rs = cursor.fetchall()
permissions = [ValuePermission(row['value']) for row in rs]
            