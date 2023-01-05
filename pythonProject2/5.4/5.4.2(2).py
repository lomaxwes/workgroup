def line_equation(a, b):
    if a:         # эта строка означает если a = True (a != 0)
        return  b / a
    elif not a and not b:
        return "Бесконечное количество корней"
    else:         #  иначе a = False ( a = 0 )
        return "Нет корней"

print(line_equation(0, 0))