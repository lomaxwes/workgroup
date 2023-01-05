
# Это обычная функция которая занимает много памяти, тк хранит все элементы
# def fact(n):
#     pr = 1
#     a = []
#     for i in range(1, n + 1):
#         pr = pr * i
#         a.append(pr)
#     return a
# print(fact(10))


# Напишем тоже самое только с функцией генератор

def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr = pr * i
        yield pr

for i in fact(10):
    print(i, end= ' ')
