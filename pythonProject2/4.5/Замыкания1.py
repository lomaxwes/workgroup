# def adder(value):
#
#     def inner(a):
#         return value + a
#     return inner
# a2 = adder(2)
# a5 = adder(5)
#
# print(a2(5))
# print(a5(10))

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

s = counter()
print(s())
print(s())
print(s())

d = counter()
print(d())

