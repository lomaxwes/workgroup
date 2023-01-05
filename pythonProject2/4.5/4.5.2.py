def decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    count = 0
    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        nonlocal count
        count += 1
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return print(f" Результат функции {fn.__name__} равен {result}! Функция {fn.__name__} вызывалась {count} раз.")
    return wrapper

@ decorator
def plus(a, b):
    return (a + b)



plus(1,3)
