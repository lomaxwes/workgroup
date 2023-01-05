a, count, n = [], False, 4
for i in range(n):
    a.append(input())
for i in range(n-1):
    for j in range(n-1):
        if a[i][j] == a[i+1][j] and a[i][j+1] == a[i+1][j+1]:
            count = True
print('No' if count else 'Yes')
