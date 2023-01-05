# Выражения-генераторы

b = (i**2 for i in range(1, 6))

# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
print('first')  # вызывается первый раз итерация по всем объектам генератора b
for i in b:
    print(i)
print('second')
for i in b:  # вызывается второй раз итерация по всем объектам
# генератора b и она не сработает, тк у генератора итерацию по всем объектам можно
# пройти всего лишь один раз
    print(i)

print(sum(b))    # так же не сработает
