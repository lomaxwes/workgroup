def average_numbers():
    numbers = []
    def inner(number):
        numbers.append(number)
        print(numbers)
        return sum(numbers) / len(numbers)
    return inner

r1 = average_numbers()


