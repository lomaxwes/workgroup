# работаем с приватным методом и также не можем обратиться к нему,
# то мы можем организовать получение данных через публичный метод,
# например:


class BankAccount:

    def __init__(self, name, balance, passport):
      self.__name = name
      self.__balance = balance
      self.__passport = passport

    def public_call(self):
      print('work public method')
      self.__print_private_data()

    def __print_private_data(self):
      print('work private method')
      print(self.__name, self.__balance, self.__passport)



account1 = BankAccount('Bob', 100000, 45484564654)
account1.public_call()

