def sum_all(n):
    if n == 0:
        return False
    return sum_all(n - 1) + n

print(sum_all(4))
