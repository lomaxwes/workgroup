class Room1:
    def get_room(self):
        print('room1')


class Room2:
    def get_room(self):
        print('room2')

    def get_room2(self):
        print('room2 for flat')


class Kitchen:
    def get_kitchen(self):
        print('kitchen')


class Flat(Kitchen, Room1, Room2):
    ...


f = Flat()
f.get_kitchen()
f.get_room()
f.get_room2()

# Класс Flat наследует классы отдельных комнат в следующем порядке: Kitchen, Room1, Room2. Это значит,
# что поиск методов при их вызове (f.get_kitchen() и др.) сначала будет осуществляться в классе Kitchen,
# затем, если метод не найден, в классе Room1, и только затем Room2. Это хорошо видно на примере вызова метода get_room().
#
# Также заметим, что наследуемый класс Flat также будет определяться, как Kitchen, Room1, Room2 в функции isinstance:


print(isinstance(f,Flat))
print(isinstance(f,Room1))
print(isinstance(f,Room2))