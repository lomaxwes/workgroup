n = int(input())  # таймлимит не пройти!!!!!!!!!
_sum = 0
for i in range(n+1, 2*n):
    count = 0
    s = 1
    k = 0
    while s <= i and k < 3:
        if i % s == 0:
            k += 1
        s += 1
    if k == 2:
        _sum += 1
print(_sum)
