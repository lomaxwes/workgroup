def divisors_number(a):
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1
    return count

divisors_number(6)
divisors_number(5)
divisors_number(4)
outside_6 = divisors_number(6)
outside_5 = divisors_number(5)
outside_4 = divisors_number(4)
print(outside_6)
print(outside_5)
print(outside_4)