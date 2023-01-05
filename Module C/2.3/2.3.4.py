class Square:
    _x = None

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x > 0:
            self._x = x
        else:
            raise ValueError("Отрицательное число")

    @property
    def area(self):
        return self.x**2


area5 = Square(5)
area_5 = Square(-5)
print(area_5.area)