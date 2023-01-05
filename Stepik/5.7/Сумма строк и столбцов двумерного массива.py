n, m = map(int, input().split())
a = []
sum1 = 0
sum2 = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    sum1 = 0
    for j in range(m):
        sum1 += a[i][j]
    print(sum1, end=' ')
print()
for j in range(m):
    sum2 = 0
    for i in range(n):
        sum2 += a[i][j]
    print(sum2, end=' ')