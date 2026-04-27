from enum import Enum

class ValuePermission(Enum):
    CUSTOMER_EDIT = 1
    CUSTOMER_DELETE = 2
    TRANSACTION_COMMIT = 3
    ACCOUNT = 4