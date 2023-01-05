# Квадратичная функция y = a*x**2 + b*x + c, где а != 0.

def quatro (a, b, c):
    return lambda x: (a * x ** 2) + b * x + c

kvadro_f = quatro(2, 3, 4)
print(kvadro_f(2))

# Функция гиперболы y=k/х

def hyperbole (k):
    return lambda x: k / x

hyp = hyperbole(4)

print(hyp(2))





