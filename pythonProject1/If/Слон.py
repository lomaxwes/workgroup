x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())

if (1 <= x1 <= 8) and (1 <= y1 <= 8) and (1 <= x2 <= 8) and (1 <= y2 <= 8):
    if abs(x1 - x2) == abs(y1 - y2):
        print("YES")
    else:
        print("NO")
else:
    print("Введите корректные координаты!")
