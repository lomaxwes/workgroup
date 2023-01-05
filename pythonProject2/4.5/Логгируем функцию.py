def logger(func):
    def wrap(*args,**kwargs):
        result = func(*args,**kwargs)
        log = f"args: {', '.join(map(str,args))} , result: {result}"
        wrap.logs.append(log)
        return result
    wrap.logs = []
    return wrap

@logger
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 2) + fib(n -1)

fib(5)
print(fib.logs)