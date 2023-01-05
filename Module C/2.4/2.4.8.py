
try:
    last = int(input("Введите число: "))

except ValueError:
    print("Вы ввели неправильное число")

else:
    print(f"Вы ввели {last}")

finally:
    print("Выход из программы")


