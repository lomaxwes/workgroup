class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return f"Площадь прямоугольника равна: {self.a * self.b}"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return f"Площадь квадрата равна: {self.a ** 2}"
# возведение в степень **2 (в квадрат)


class Circle:
    def __init__(self, a):
        self.a = a

    def get_circle_square(self):
        return f"Площадь круга равна: {self.a**2*3.14}"


