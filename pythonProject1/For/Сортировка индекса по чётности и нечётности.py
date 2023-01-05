a = [23, 11, 33, 44, 22, 18, 32, 4, 7, 29, 4]
chet_i = []
necht_i = []
n = len(a)
for i in range(n):
    if a[i] % 2 == 0:
        chet_i.append(i)
        chet_i.append(i + 1) # 
    else:
        necht_i.append(i)
print(chet_i)
print(necht_i)

