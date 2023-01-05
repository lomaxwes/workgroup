
def rec(n):
    sum_ = 0
    if n == 0:
        return False
    if 0 < n < 10:
        return n
    if n > 9:
        for i in n:
            sum_ = (n // 10) + (n % 10)
            return n


print(rec(1235))
