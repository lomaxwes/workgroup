x1 = 2
y1 = 3
x2 = 5
y2 = 6
if (1 <= x1 and y1 and x2 and y2 <= 8):
    if abs(x1 - x2) == abs(y1 - y2):
        print("YES")
    else:
        print("NO")
else:
    print("Введите корректные координаты!")

