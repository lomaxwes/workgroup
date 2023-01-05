# if x > 0:
#    if y > 0:               # x > 0, y > 0
#         print("Первая четверть")
#    else:                   # x > 0, y < 0
#         print("Четвертая четверть")
#else:
#   if y > 0:               # x < 0, y > 0
#         print("Вторая четверть")
#    else:                   # x < 0, y < 0
#         print("Третья четверть")
x = 3
y = -2
if x > 0 and y >0:
    print("Первая четверть")
if x > 0 and y < 0:
    print("Четвертая четверть")
if x < 0 and y > 0:
    print("Вторая четверть")
if x < 0 and y < 0:
    print("Третья четверть")

