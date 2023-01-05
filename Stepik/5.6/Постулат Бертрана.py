n = int(input())
count = 0
for i in range(n+1, 2*n):
    if i != 2 and i % 2 ==0:
        continue
    j = 3
    flag = True
    while j * j <= i:
        if i % j == 0:
            flag = False
            break
        j += 2
    if flag:
        count += 1
print(count)
