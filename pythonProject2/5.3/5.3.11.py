# a = input("Введите числа: ")
# numbers = list(map(int,a.split()))
#
# b = []
# for i in numbers:
#     if i == 0:
#         break
#     else:
#         b.append(i)
# print(numbers == b)

L = list(map(int, input().split()))

print(all(L))


