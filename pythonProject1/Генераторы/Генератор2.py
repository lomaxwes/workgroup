# Приводим к int

# a = input()  # вводим числа через пробел
# print(type(a))  # получаем строку

a = input().split()  # разделяем элементы

a = [int(i) for i in a] # преобразуем все элементы в int
print(a)

