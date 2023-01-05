class Vector:

    def __init__(self, *args):
        a = []
        list = args
        for x in list:
            if isinstance(x, int):
                a.append(x)
        sorted(a)
        b = tuple(a)
        self.values = b

    def __str__(self):
        if self.values:
            return f"Вектор{self.values}"
        else:
            return f"Пустой вектор"


v1 = Vector(1, 2, 3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"

