
L = [i for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10,0,-1)]

N = [ ]

for i in range(10):
    N.append(L[i] * M[i])
print(N)


for a in zip(L,M):
    print(a)

for a, b in zip(L,M):
    print('a =', a, 'b =', b)