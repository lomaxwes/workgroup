def delitel(a):
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1
            print(f"{i} является делителем числа {a}")
    print(f"Количество делителей числа равно: {count}")

delitel(60)
