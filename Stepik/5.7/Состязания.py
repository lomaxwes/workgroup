a = []
n, m = map(int, input().split())
for i in range(n):
    a.append(sum(list(map(int, input().split()))))
print(f"{max(a)}\n{a.index(max(a))}")

