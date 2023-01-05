from string import digits
from string import ascii_uppercase
from string import ascii_lowercase
from string import ascii_letters


class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def check_password_dictionary(pas):
        if pas in open(r'easy_passwords.txt').read():
            return True

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

    @staticmethod
    def is_include_digit(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        for symbol in password:
            if symbol in ascii_lowercase or symbol in ascii_uppercase:
                return True
        return False

    @staticmethod
    def is_include_only_latin(password):
        for symbol in password:
            if symbol in ascii_letters:
                return True
        return False

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pass):
        if not isinstance(new_pass, str):
            raise TypeError("Пароль должен быть строкой")
        if len(new_pass) < 4 or len(new_pass) > 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(new_pass):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(new_pass):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(new_pass):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(new_pass):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = new_pass

r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # здесь хороший логин
# print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# # теперь пытаемся запись плохие пароли
# r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
# r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
r1.password = 'Hello1QEWq'  # raise TypeError("Пароль должен быть строкой")