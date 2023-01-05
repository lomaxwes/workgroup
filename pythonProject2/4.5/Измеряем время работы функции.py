import time

def timer(func):
    def wrap(*args,**kwargs):
        t0 = time.time()
        result = func(*args,**kwargs)
        t1 = time.time()
        print(f"Функция выполнялась {round(t1 - t0, 5)} секунд")
        return result

    return wrap

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 2) + fib(n -1)

@ timer
def get_fib(n):
    return fib(n)

get_fib(40)