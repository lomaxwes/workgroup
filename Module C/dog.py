from cat import Cat

class Dog(Cat):
    def get_pet(self):
        return f"Имя: {self.get_name()}, возраст: {self.get_age()}"

dog1 = Dog("Эма", 'Девочка', 3)

print(dog1.get_pet())





