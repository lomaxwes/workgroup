# e_n = (1 + 1/n)**n

def e():
    n = 10000

    while True:
        yield (1 + 1 / n) ** n
        n += 1

a = e()

print(next(a, "конец"))
print(next(a, "конец"))
print(next(a, "конец"))
print(next(a, "конец"))
print(next(a, "конец"))
print(next(a, "конец"))
print(next(a, "конец"))
print(next(a, "конец"))
print(next(a, "конец"))
print(next(a, "конец"))
