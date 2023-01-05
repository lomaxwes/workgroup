def sum_all(n):
    if n == 0:
        return False
    return n + sum_all(n - 1)

print(sum_all(5))