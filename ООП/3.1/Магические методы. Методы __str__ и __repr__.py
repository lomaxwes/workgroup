class Vector:
    def __init__(self, *args: int):
        a = []
        for x in args:
            if isinstance(x, int):
                a.append(x)
        self.values = sorted(a)

    def __str__(self):
        if len(self.values) == 0:
            return f"Пустой вектор"
        else:
            return f"Вектор{tuple(self.values)}"
v1 = Vector(4, 3, 2)
v2 = Vector()


print(v1)
print(v2)