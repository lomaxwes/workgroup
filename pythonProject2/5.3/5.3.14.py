# Модифицируйте последний пример таким образом, чтобы # в список
# сохранялось True, если элемент чётный, и False, если элемент нечётный.

L = [int(input()) % 2 == 0 for i in range(5)]
print(L)