# Генерация списков, обход строк,
# рандомный генератор чисел, условия в списках.

a = [1 for i in range(7)]
print(a)

a = [i for i in range(10)]
print(a)

a = [i**2 for i in range(1, 15)]
print(a)

a = [i//4 for i in range(1, 15)]
print(a)

a = [i for i in 'hello']
print(a)

a = [i*3 for i in 'hello']
print(a)

a = [ord(i) for i in 'hello']   # код символа в таблице ASCII
print(a)

import random   # импорт рандом

a = [ord(i) for i in 'abcde']   # код символа в таблице ASCII
print(a)

a = [random.randint(-10, 10)  for i in range(10)]
print(a)

# b = [abs(elem) for elem in a]  # пробежались по списку а с модулем числа.
# print(b)

a = [elem + 1 for elem in a]
print(a)

a = [elem**2 for elem in a]
print(a)

a = [random.randint(-10, 10)  for i in range(10)]
print(a)

b = [elem for elem in a if elem > 0] # выбираем из списка а только положительные элементы
print(b)

b = [elem for elem in a if elem % 2 == 0 and elem % 3 == 0] # выбираем из списка а,
# только четные элементы (делятся на 2) и которые делятся на 3
print(b)

