class Vector:


    def __init__(self, *args):
        args = list(filter(lambda x: isinstance(x, int), args))
        self.value = sorted(args)

    def __str__(self):
        if self.value:
            return f"Вектор {tuple(self.value)}"
        else:
            return "Пустой вектор"


v1 = Vector(6, 7.7, 3, 1)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"