a, b, wrong = [], [], 0
n, m = map(int, input().split())
for i in range(n):
    a.append(input())
input()
for i in range(n):
    b.append(input())
for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            wrong += 1
print(wrong)




