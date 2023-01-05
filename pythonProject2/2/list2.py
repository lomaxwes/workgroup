letters = ['a', 'b', 'c', 'd']
letters.append('e')
print(letters[-1])
print(len(letters))  # длина списка
print(letters[len(letters)-1]) # доступ к последнему элементу можно получить, если уменьшить эту длину на 1
letters.append('f') # добавляем ещё одну букву
letters.append('g') # и ещё одну
print(letters[-1]) # g
print(letters[-4]) # d
letters.pop() # вызов метода без аргументов удаляет последний элемент списка
print(letters)  # ['a', 'b', 'c', 'd', 'e', 'f']  # был удалён последний элемент
letters.pop(0)
print(letters) # ['b', 'c', 'd', 'e', 'f'] # был удалён нулевой элемент
letters.pop(3) # и необязательно удалять из начала или конца списка
print(letters) # ['b', 'c', 'd', 'f'] # был удалён элемент с индексом 3
new_let = letters[::2]
print(new_let)  # Задает шаг, через который извлекаются элементы
