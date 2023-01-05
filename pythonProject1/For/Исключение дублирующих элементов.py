a = [25, 15, 45, 35, 15, 55, 45]
b = []
for i in a:
    if not i in b:
        b.append(i)
print(b)