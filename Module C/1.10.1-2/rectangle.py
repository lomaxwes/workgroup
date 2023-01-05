class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f" Rectangle: {self.x}, {self.y}, {self.width}, {self.height}."  # print(r1)

    def get_str(self):
        return f" Rectangle: {self.x}, {self.y}, {self.width}, {self.height}."  # print(r1.get_str())

    def get_square(self):
        return self.width * self.height

r1 = Rectangle(5, 10, 50, 100)


print(r1)

print(r1.get_str())

print(r1.get_square())