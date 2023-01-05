# Мой вариант
a = 0
while True:
    a += 1
    b = a + 1 - 1
    print(b)
    if id(a) != id(b):
        break

 # Вариант скилл фэктори
a = 0
b = 0

while id(a) == id(b):
    a -= 1
    b -= 1

print(a)