a, b, c, d = [], [], [], []
n, m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))
for i in a:
    b.append(max(i))
    c.append(sum(i))
if b.count(max(b)) == 1:
    print(b.index(max(b)))
elif b.count(max(b)) > 1:
    for i in a:
        if max(b) in i:
            d.append(sum(i))
    if max(d) in c:
        print(c.index(max(d)))