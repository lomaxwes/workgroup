digits = [value for value in range(1, 21)]
print(digits)

digits = list(range(1, 21))
print(digits)

digits = []
for value in range(1, 21):
    digit = value
    digits.append(digit)
print(digits)

digits = []
for value in range(1, 21):
   digits.append(value)
print(digits)

digits = [value for value in range(1, 1000001)]
print(max(digits), min(digits))
print(sum(digits))

digits = [value for value in range(1, 20, 2)]
print(digits)

digits = [value for value in range(3, 31, 3)]
print(digits)

digits = []
for value in range(1, 31):
    digit = (value % 3 ==0)
    digits.append(digit)
print(digits)

digits = [value**3 for value in range(1, 11)]
print(digits)

digits = []
for value in range(1, 11):
    #digit = value**3               # и так и так верно digit = value**3 + digits.append(digit)
    digits.append(value**3)         # и так верно
print(digits)

