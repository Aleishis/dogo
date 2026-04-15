from datetime import datetime
from enums.transaction_type import TransactionType
from persistance.db import get_connection
import pymysql

class Transaction():
    
    def __init__(self,id:int,date:datetime, amount:float, type:TransactionType, description:str):
        
        self.id = id
        self.date = date
        self.amount = amount
        self.type = type
        self.description = description
    
    
    def get_transactions_by_account(user_id:int):
        
        try:
        
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            
            query = "SELECT id, date, amount, type, description FROM transactions WHERE user_id = %s"
            
            cursor.execute(query, (user_id,))
            
            rs = cursor.fetchall()
                        
            cursor.close()
            connection.close()
            
            return rs
            
        except Exception as ex:
            print("Algo salio mal al conseguir las transactions", ex)
        