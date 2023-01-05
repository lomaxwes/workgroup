def line_equation(a, b):
    if a:         # эта строка означает если a = True (a != 0)
       return  b / a
    else:         #  иначе a = False ( a = 0 )
        return "Нет корней"

print(line_equation(0, 1))