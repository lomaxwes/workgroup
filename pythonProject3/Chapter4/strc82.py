my_t = (3, )
print(my_t)

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print('original demensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

print(dimensions + dimensions)

menus = ('борщ', 'рассольник'), ('курица', 'гуляш'), ('шашлык',)
for menu in menus:
    print(menu)
menus = ('суп гороховый', 'суп лапша'), ('курица', 'гуляш'), ('шашлык',)
for menu in menus:
    print(menu)