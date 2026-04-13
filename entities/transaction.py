from datetime import datetime
from enums.transaction_type import TransactionType

class Transaction():
    
    def __init__(self,id:int,date:datetime, amount:float, type:TransactionType, description:str):
        
        self.id = id
        self.date = date
        self.amount = amount
        self.type = type
        self.description = description