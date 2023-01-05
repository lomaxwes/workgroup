n = int(input())
a = []
count1 = 0
count2 = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if j != i:
            if a[i][j] == a[j][i]:
                count1 += 1
            else:
                count2 += 1


if count2 > 0:
    print("No")
else:
    print("Yes")