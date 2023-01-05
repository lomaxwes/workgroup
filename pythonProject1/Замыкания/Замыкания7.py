def add(a, b):
    return a + b

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функия {func.__name__} вызывалась {count} раз")
        return func(*args, **kwargs)

    return inner
