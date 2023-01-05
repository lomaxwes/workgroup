print(list(map(lambda x: x ** 2, range(1, 11))))

a = list(map(lambda x: x ** 2, range(1, 11)))

print(a)

d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}

# Чтобы отсортировать его по ключам, нужно сделать так
print(dict(sorted(d.items())))
# {1: 'd', 2: 'c', 3: 'b', 4: 'a'}

print(sorted(d.items(), key=lambda x: x[1]))  # сортировка словаря
# по второму значению


