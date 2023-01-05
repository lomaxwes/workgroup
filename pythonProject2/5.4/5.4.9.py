number = [2, 20, 3, 4, 7]


def rec(number):
    if len(number) == 1:
        return number[0]
    return number[0] if number[0] < rec(number[1:]) else rec(number[1:])

print(rec(number))