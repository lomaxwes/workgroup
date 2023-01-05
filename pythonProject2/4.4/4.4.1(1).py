
def gen_num(a, b):
    n = 1
    while True:
        n += a + b
        for i in range(a, n, b):
            yield i

for num in gen_num(20, 20):
    print(num)
# s = gen_num(20, 20)
# print(next(s))
# print(next(s))
# print(next(s))


