import math

a = input()
s = math.ceil(len(a) // 2)  # или можно использовать хитро (len(a)+1) // 2 без мат функции
print(a[s:]+a[:s])

