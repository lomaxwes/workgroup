def decor(func):
    count = 0
    def wrap(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функция {func.__name__} вызывалась {count} раз")
        return func(*args, **kwargs)

    return wrap


@decor
def rec(x):
    if x < 4:
        print(x)
        rec(x + 1)
        print(x)
rec(1)


# def plus(a, b):
#     return a + b
#
# print(plus(1, 2))
# print(plus(1, 2))
# print(plus(3, 2))
