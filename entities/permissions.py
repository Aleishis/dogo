from enums.value_permission import ValuePermission

class Permission:
    def __init__(self, id: int, value: ValuePermission, id_user: int):
        self.id = id
        self.value = value
        self.id_user = id_user