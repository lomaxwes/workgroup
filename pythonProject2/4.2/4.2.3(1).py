def delit(n):
    a = int(input("Введите делимое число:\n"))  # делимое
    if a % n == 0:
        print(f"{n} является делителем числа {a}")
    else:
        print(f"{n} не является делителем числа {a}")

delit(8)