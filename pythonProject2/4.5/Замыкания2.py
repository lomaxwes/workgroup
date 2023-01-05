def average_numbers():
    numbers = []
    def  inner(number):
        numbers.append(number)
        print(numbers)
        return sum(numbers) / len(numbers)
    return inner

s1 = average_numbers()

print(s1(5))
print(s1(10))
print(s1(15))

s2 = average_numbers()
print(s2(100))
