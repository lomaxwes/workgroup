a = []
maxi = 0
n, m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))

for i in a:
    if maxi < max(i):
        maxi = max(i)

for i in range(n):
    for j in range(m):
        if maxi == a[i][j]:
            stroka = i
            stolb = j

for i in range(n):
    for j in range(m):
        if maxi == a[i][j] and stroka >= i:
            stroka = i
            stolb = j
print(f"{maxi}\n{stroka} {stolb}")