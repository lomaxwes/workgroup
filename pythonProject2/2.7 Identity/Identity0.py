L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

a = 5
b = 3+2
print(id(a))
print(id(b))

print(id(a)-id(b))  # Какое значение идентичности будут иметь объекты данных, хранящиеся в этих переменных?