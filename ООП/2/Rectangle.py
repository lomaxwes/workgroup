class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length


r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)

print(r1.area) # 15
print(r2.area) # 6