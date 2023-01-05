class Student:
    def __init__(self, __name, __age, __branch):
        self.__name = __name
        self.__age = __age
        self.__branch = __branch

    def __display_details(self):
        print(f"Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}")

    def access_private_method(self):
        return self.__display_details()

obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()