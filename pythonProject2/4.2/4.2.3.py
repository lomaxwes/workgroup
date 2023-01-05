def divider_number(a, n):
    if a % n == 0:
        print(f"{n} - является делителем {a}")
    else:
        print(f"{n} - не является делителем {a}")

divider_number(10, 3)
divider_number(57, 3)