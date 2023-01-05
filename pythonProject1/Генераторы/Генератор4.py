# двойные циклы

a = [(i, j) for i in 'abc' for j in [1, 2, 3]]

print(a)

b = [i*j for i in [2, 3, 4, 5] for j in [1, 2, 3] if i * j >= 10]
print(b)

c = [i**3 for i in range(1, 11)]
print(c)