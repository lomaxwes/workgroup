def average_numbers():
    summa = 0
    count = 0

    def  inner(number):
        nonlocal summa
        nonlocal count
        summa += number
        count += 1
        return summa / count
    return inner

s1 = average_numbers()

print(s1(10))
print(s1(20))

s2 = average_numbers()
print(s2(20))
print(s2(2))
