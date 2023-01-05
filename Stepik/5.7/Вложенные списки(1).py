n = int(input())
a = []
_sum = 0
for i in range(n):
   a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i] == a[j]:
            _sum += a[i][j]
print(_sum)