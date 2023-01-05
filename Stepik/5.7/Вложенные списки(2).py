n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i < j:
            a[j][i], a[i][j] = a[i][j], a[j][i]
for i in a:
    print(*i)
