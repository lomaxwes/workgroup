a = int(input("Введите число: "))

#  Первый вариант
# if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
#     print("Число подходит под условия")

# Вариант с функцией all

if all([type(a) == int,
    100 <= a <= 999,
    a % 2 == 0,
    a % 3 == 0]):
    print("Число подходит под условия")
else:
    print("Не удовлетворяет условиям")

# if a > 100:
#     if a < 999:
#         if a % 2 == 0:
#             if a % 3 == 0:
#                 print("Ура!")
#             else:
#                 print("Не делится на 3")
#         else:
#             print("Не делится на 2")
#     else:
#         print("Больше 999")
# else:
#     print("Меньше 100")