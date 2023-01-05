def add(a, b):
    return a + b

def counter(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функция {func.__name__} вызывалась  {count} раз ")
        return func(*args, **kwargs)
    return inner

a = counter(add)

def mult(a, b, c):
    return a*b*c

m = counter(mult)