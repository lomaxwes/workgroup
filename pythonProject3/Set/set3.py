a = set(map(int, input("Введите числа: ").split()))
b = set(map(int, input("Введите числа: ").split()))
#a_set = {1, 2, 3, 4}
#b_set = {1, 5, 6, 7, 8}
b_minus_a = a.symmetric_difference(b)
print(b_minus_a)

