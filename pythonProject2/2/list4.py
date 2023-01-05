z = [7, 3, 3]
z.extend([4,5])
print(z)
print([1,2] + [3,4])
print([z]+[3,4]) # добавляет к списку z новый список [3,4]
print(z)
y = [z]+[3,4]
print(len(y))
print(y)
y.pop(1)
y.pop(1)
print(y)
z.insert(4,[1,2])
print(z)
z.pop(4)
print(z)
