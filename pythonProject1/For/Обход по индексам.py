a = [25, 35, 45, 15, 15, 55]

n = len(a)
for i in range(n):
    print(i, a[i])
    a[i] += 5
print(a)