letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters.index('f', 3))  # ищет 'f', начиная с 3-го элемента

num = [3, 4, 6, 5, 4, 5, 6, 7, 7, 3, 4]
print(num.count(4))  # метод count считает сколько раз в списке записано число - 4.
num.sort()
print(num)
num.sort(reverse = True)
print(num)
num.sort(reverse = False)
print(num)
names = ["Стив", "Рейчел", "Майкл", "Адам", "Джессика", "Лестер"]
names.sort()
print(names)
names.append("Егор")
print(names)
num.remove(7)
print(num)
names3 = names.pop(3)
print(names3)
print(names)
num.extend([9, 10])
print(num)
print