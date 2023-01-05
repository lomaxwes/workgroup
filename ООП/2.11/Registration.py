class Registration:
    def __init__(self, login):
        self.login = login

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value: str):
        if value.count('@') != 1:
            raise ValueError("Логин должен содержать один символ '@'")
        if '.' in value:
            if value.index('@') > value.index('.'):
                raise ValueError("Логин должен содержать символ '.'")
        else:
            raise ValueError("Login must include at least one ' @ '")
        self.__login = value

# r1 = Registration('qwerty@rambler.ru') # здесь хороший логин
# print(r1.login)  # qwerty@rambler.ru

# теперь пытаемся запись плохой логин
# r1.login = '123456'  # ValueError("Логин должен содержать один символ '@'")
#
# r2 = Registration('qwerty.ru')  # ValueError("Логин должен содержать один символ '@'")
# print(r2.login)
r3 = Registration('qwerty@ru')  # ValueError("Логин должен содержать символ '.'")