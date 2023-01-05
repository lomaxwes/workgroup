A = int(input("Введите число А  :\n"))
B = int(input("Введите число B:\n"))
C = int(input("Введите число C:\n"))
if ((A < 45) and (B >= 45) and (C >=45)) or ((B < 45) and (A >= 45) and (C >=45)) or ((C < 45) and (A >= 45) and (B >=45)):
    print(True)
else:
    print(False)

