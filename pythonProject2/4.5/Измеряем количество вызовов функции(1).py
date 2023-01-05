def counter(func):
    def wrap(*args,**kwargs):
        wrap.num_calls += 1
        result = func(*args,**kwargs)
        return result
    wrap.num_calls = 0
    return wrap

@counter
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 2) + fib(n -1)

print(fib(10))

print(fib.num_calls)


def wrap(n):
    wrap.sum += n
    print(wrap.sum)
wrap.sum = 0

