def fib():
    a, b = 0, 1
    yield a  # F0
    yield b  # F1

    while True:
        a, b = b, a + b
        yield b

s = fib()
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))


