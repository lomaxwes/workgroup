n = int(input())
count = 1
for i in range(n + 1, 2 * n):
    count += 1
    list = []
    while count * count <= n:
        if i % count == 0:
            list.append(i)
            if count != i:
                list.append(i // i)
        count += 1
print(len(list))

