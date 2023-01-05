from see_battle import Dot

class Ship:

    def __init__(self, bow, len, head):
            self.bow = bow
            self.len = len
            self.head = head


    def dots(self):
        ship_list = []
        for i in range(self.len):
            new_x = self.bow.x
            new_y = self.bow.y

            if self.head == 0:
                new_x += i

            elif self.head == 1:
                new_y += i

            ship_list.append(Dot(new_x, new_y))

        return ship_list


