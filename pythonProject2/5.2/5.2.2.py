L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))


a = 0
b = 0
print(id(a))
print(id(b))
print(id(a) - id(b))