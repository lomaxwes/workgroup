def adder(value):
    def inner(a):
        return a + value
    return inner