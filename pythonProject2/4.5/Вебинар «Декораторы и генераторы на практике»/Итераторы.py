# a = [1,2,3,10]
#
# iterator = iter(a)
#
# print(next(iterator,"Конец!"))
# print(next(iterator,"Конец!"))
# print(next(iterator,"Конец!"))
# print(next(iterator,"Конец!"))
# print(next(iterator,"Конец!"))
def gen(n):
    for i in range(1, n):
        yield i

s = gen(6)

print(s)
print(next(s))
print(next(s))
print(next(s))
print(next(s))

# print(next(gen()))
# print(next(gen()))
# print(next(gen()))
# print(next(gen()))