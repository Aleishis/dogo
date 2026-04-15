from datetime import datetime
from entities.user import User
from persistance.db import get_connection
from entities.transaction import Transaction
import pymysql


class Account():
    
    def __init__(self, id: int, created_at: datetime, user:User, number:str, transactions:list):
        
        self.id = id
        self.created_at = created_at
        self.user_id = user
        self.number = number
        self.transactions = transactions
        
    
    def get_account_by_user(user_id:int):
        
        try:
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            
            query = 'SELECT id, number, created_at, user_id FROM accounts WHERE id = %s'
            
            cursor.execute(query, (user_id,))
            
            rs = cursor.fetchone() #result set
            
            user = User.get_by_id(rs['user_id'])

            transactions = Transaction.get_transactions_by_account(rs['id']) #TODO

            account = Account(
                id=rs['id'],
                created_at=rs['created_at'],
                user=user,
                transactions=transactions,
                number=rs['number']
                )
            
            return account
        except Exception as ex:
            print("Algo salio mal al solicitar un account")
            print(ex)
            
            
            