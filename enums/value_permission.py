from enum import Enum

class ValuePermission(Enum):
    CUSTOMER_EDIT = 1
    CUSTOMER_DELETE = 2
    TRANSACTION_COMMIT = 3
    ACCOUNT = 4
    SEE_LOGS = 5
    INSURANCE = 6
    CREDIT_CARD = 7
    CARDLESS_WITHDRAWAL = 8
    
    
    def get_all_permissions():
        return [p.value for p in ValuePermission] #TRAE LOS VALORES DE LOS PERMISSIONS, NO LOS NOMBRES, PORQUE EN LA DB SE GUARDAN LOS VALORES