class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        return self.__name, self.__balance, self.__passport


account1 = BankAccount('Bob', 100000, 45484564654)
print(account1.print_private_data())

# print(account1.__name) # AttributeError
# print(account1.__balance) # AttributeError
# print(account1.__passport)  # AttributeError

