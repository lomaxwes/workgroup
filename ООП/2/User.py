class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        if role in Access.__access_list():
            return True
        return False

    @staticmethod
    def get_access(user_obj):
        if isinstance(user_obj, User):
        if

            print(f"{user_obj.name}")






user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"

# zaya = User('milaya_zaya999', 'user')
# Access.get_access(zaya) # печатает AccessDenied
#
# Access.get_access(5)