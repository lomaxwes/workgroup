# a1 = [1, 4, 2]
# k = tuple(a1)  # перевод списка в кортеж


# Циклически сдвинуть элементы списка "вправо",
# чтобы получить [7, 1, 2, 3, 4, 5, 6]

A = [1, 2, 3, 4, 5, 6, 7]
# Я сделал
A.pop(6)
A[:0] = [7]
print(A)
# Пример решения skillfactory

A[-1:] + A[:-1]
print(A)

# Поменять максимальный и минимальный элемент списка
B = [1, 2, 3, 4, 5, 6, 7]
max_index = B.index(max(B))
min_index = B.index(min(B))
B[max_index], B[min_index] = B[min_index], B[max_index]
print(B)