
# ВЫВЕСТИ СУММУ НАТУРАЛЬНЫХ ЧИСЕЛ ИЗ ЧИСЛА N
def sum_num(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_num(n // 10)



print(sum_num(-123))
print(sum_num(0))
print(sum_num(123))
