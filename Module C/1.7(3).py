class Room:
    def get_room(self):
        print('room')


class Room1(Room):
    def get_room(self):
        print('room1')


class Room2(Room):
    def get_room(self):
        print('room2')


class Flat(Room1, Room2):
    ...


print(Flat.mro())  # метод класса, который показывает порядок наследования

f = Flat()
f.get_room()

# Обратите внимание на метод mro(), он относится к методам класса, а не объекта класса, поэтому вызывается непосредственно от Flat.
# Метод mro() возвращает порядок, в котором будут проинспектированы родительские классы. Методы класса будут подробно рассмотрены в следующем модуле.