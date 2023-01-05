a, count, n = [], 0, int(input())
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i+1, n):
        if a[i][0] == a[j][1]:
            count += 1
        if a[i][1] == a[j][0]:
            count += 1
print(count)
