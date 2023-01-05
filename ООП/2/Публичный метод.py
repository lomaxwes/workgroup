class BankAccount:

    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_data(self):   # эти данные доступны из общих вызовов
        print(self.name, self.balance, self.passport)


account1 = BankAccount('Bob', 100000, 45484564654)
account1.print_data()
print(account1.name)
print(account1.balance)
print(account1.passport)
