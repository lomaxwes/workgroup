# def f():
#     return [43, 65, 32]

def genf():
    s = 0
    for i in [43, 65, 32]:
        yield i
        print(s)
        s = s * 10 + 0

g = genf()



print(next(g, 'конец'))
print(next(g, 'конец'))
print(next(g, 'конец'))
print(next(g, 'конец'))
print(next(g, 'конец'))
print(next(g, 'конец'))
print(next(g, 'конец'))

