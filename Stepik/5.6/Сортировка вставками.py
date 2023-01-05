n = int(input())
s = list(map(int, input().split()))
for i in range(1, n):
    for j in range(i, 0, -1):
        if s[j] < s[j-1]:
            s[j], s[j-1] = s[j-1], s[j]
        else:
            break
print(*s)