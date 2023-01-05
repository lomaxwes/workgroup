n = int(input("Введите число для расчёта факториала:\n"))
F = 1
for num in range(1, n + 1):
     F *= num
print(f"Факториал числа {n} равен: {F}")
