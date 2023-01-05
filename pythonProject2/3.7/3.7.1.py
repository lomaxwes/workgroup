list_ = [-5, 2, 4, 8, 12, -7, 5]
# Объявим переменную, в которой будем хранить индекс отрицательного элемента
index_negative = None

for i, value in enumerate(list_):
    if list_[i] < 0:
        index = i
print(f"Индекс последнего отрицательного числа: {index}")






