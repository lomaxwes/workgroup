
# Найдите ошибку в коде и перепишите строку с ошибкой полностью.
# Представленная ниже программа должна находить множество символов,
# которые встречаются в двух строках одновременно.

a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.intersection(b_set)  # изначальный вариант был a_and_b = a_set.union(b_set)

print(a_and_b)