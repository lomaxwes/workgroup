a, maxi = [], []
n, m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))
for i in a:
    maxi.append(max(i))
print(maxi.count(max(maxi)))
