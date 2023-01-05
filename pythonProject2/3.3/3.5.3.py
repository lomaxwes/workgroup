# У вас есть заготовка функции — def get_wind_class(speed):
# Вам нужно вместо "???" написать цикл, который возвращает из функции класс ветра в зависимости от его характера:
# от 1 до 4 м/с - "weak [1]"
# от 5-10 м/c - "moderate [2]"
# от 11-18 м/c - "strong [3]"
# от 19 м/c - "hurricane [4]"
# В последней строке мы просим программу напечатать результат (в зависимости от цифры в скобках) —
# def get_wind_class(speed):  # Объявление функции

# print(get_wind_class(3))  # Печатаем результат выполнения
speed = int(input())
week = list(range(1, 5))
moderate = list(range(5, 11))
strong = list(range(11, 19))
hurricane = list(range(19, 100))
if speed in week:
    print("weak")
elif speed in moderate:
    print("moderate")
elif speed in strong:
    print("strong")
elif speed in hurricane:
    print("hurricane")
