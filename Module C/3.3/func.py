PI = 3.14

def square_rectangle(a, b):
    return a * b


def square_circle(r):
    return PI * r**2

if __name__ == '__main__':
   # проверяем работоспособность функции, дальнейшая часть не будет импортирована
   assert square_circle(5) == 78.5  # если ответы будут отличаться, то будет вызвана ошибка
   assert square_rectangle(5, 4) == 20
