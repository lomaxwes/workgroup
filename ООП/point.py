from math import sqrt

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, object):
        if isinstance(object, Point):
            return f"Передана не точка"
        else:
            return sqrt(((self.x - object.x)**2 + (self.y - object.y)**2)**0.5)




p1 = Point()
p2 = Point()
p1.set_coordinates(50, 10)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2) # вернёт 5.0
# p1.get_distance(10) # Распечатает "Передана не точка"
