# string = input("Введите числа:")
# list_of_string = string.split() # список строковых представлений чисел
# list_of_number = list(map(float, list_of_string))  # cписок чисел
# list_of_number[-1], list_of_number[0] = list_of_number[0], list_of_number[-1]
# print(list_of_number)

# list_of_number.append(sum(list_of_number))
# print(list_of_number)

L = list(map(float, input('Введите числа:').split()))
# обмениваем первое и последнее число
# с помощью множественного присваивания
L[0], L[-1] = L[-1], L[0]
# находим сумму и добавляем её в конец списка
L.append(sum(L))
print(L)
