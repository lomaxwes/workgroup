n = int(input())
spis = list(map(int, input().split()))
count = 0
for i in range(n - 1):
    for j in range(n - 1 - i):
        if spis[i] > spis[i+1]:
            spis[i], spis[i+1] = spis[i+1], spis[i]
            count += 1
print(*spis)
print(count)
