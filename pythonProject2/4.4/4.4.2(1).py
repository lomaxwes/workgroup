

def gen(args):
    while True:
        for i in args:
            yield i

s = gen([1, 2, 3])

print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))



