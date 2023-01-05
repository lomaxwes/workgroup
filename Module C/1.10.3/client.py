class Client:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.first_name} {self.second_name}. {self.city}. Баланс: {self.balance} "  # print(clien_1)

    def get_info_client(self):
        return f"{self.first_name} {self.second_name}. {self.city}."                          #  print(clien_1.get_info_client())


clien_1 = Client('Петя', 'Фёдоров', 'Москва', 50)
clien_2 = Client('Иван', 'Петров', 'Москва', 90)
clien_3 = Client('Владимир', 'Зайцев', 'Кострома', 130)
clien_4 = Client('Олеся', 'Янина', 'Новосибирск', 40)


guest_list = [clien_1, clien_2, clien_3, clien_4]

for guest in guest_list:
    print(guest.get_info_client())