n, m = map(int, input().split())
para = 0

for a in range(1000):
    for b in range(100):
        if (a == m - b**2) and (b == n - a**2):
            para += 1
print(para)
