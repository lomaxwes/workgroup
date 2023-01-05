def casher(func):
    def wrap(*args):
        if args in wrap.cashed:
            return wrap.cashed[args]
        else:
            result = func(*args)
            wrap.cashed[args] = result
            return result
    wrap.cashed = {}
    return wrap



@casher
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 2) + fib(n -1)

print(fib(50))
print(fib.cashed)