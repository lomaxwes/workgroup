def decorator(func):
    data = {}
    def wrapper(n):
        nonlocal data
        if n in data:
            print(f"возврат из кэш {data[n]}")
        else:
            data[n] = func(n)
            print(f"добавление в кэш {data[n]}")
        print(f"Кэш {data}")
        return data

    return wrapper


@decorator
def f(n):
    return n * 123456789

f(1)
f(2)
f(3)
f(2)
