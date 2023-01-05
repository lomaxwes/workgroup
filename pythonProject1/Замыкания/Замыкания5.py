def average_numbers():
    summa = 0
    count = 0

    def inner(number):
        nonlocal count   # раз мы хотим менять переменные, значит надо объявить их nonlocal
        nonlocal summa
        summa += number
        count += 1
        return summa / count
    return inner