a = input("Введите числа:")
b = input("Введите числа:")
# a = 1 2 3 4 5 6 7 8
# b = 2 4 6 8 10 12
num_a = list(map(int, a.split()))
num_b = list(map(int, b.split()))


a_set, b_set = set(num_a), set(num_b)

all_symmet = a_set.symmetric_difference(b_set)
list_symmet = list(all_symmet)
print(list_symmet)

# Ответ  [1, 3, 5, 7, 10, 12]