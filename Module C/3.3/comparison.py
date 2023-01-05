from func import *

def main():

    a, b = map(float, input("Введите стороны прямоугольника: ").split())

    r = float(input("Введите радиус круга: "))

    if square_rectangle(a, b) > square_circle(r):
        print("Прямоугольник больше круга")
    else:
        print("Круг больше прямоугольника")

if __name__ == "main":
main()
