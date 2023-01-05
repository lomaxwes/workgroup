    # ВЫВЕСТИ СУММУ НАТУРАЛЬНЫХ ЧИСЕЛ ИЗ ЧИСЛА N

def sum_natur(n):
    if n <= 0:
        return False
    if 0 < n < 10:
        return n
    if n > 10:
        return sum_natur(n // 10) + n % 10
print(sum_natur(0))
print(sum_natur(-123))
print(sum_natur(123))



