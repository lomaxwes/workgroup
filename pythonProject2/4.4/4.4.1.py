
def nat(start = 1, step = 1):
    counter = start
    while True:
        yield counter
        counter += step


n = nat(2, 3)
print(next(n))
print(next(n))
print(next(n))

# for i in nat(2, 3):
#     print(i)

