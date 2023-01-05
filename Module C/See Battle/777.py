class Constructor:
    def add_atribute(self, *args):
        self.args = args


    def display(self):
        print(self.__dict__)

c1 = Constructor()
c2 = Constructor()
c3 = Constructor()
c1.add_atribute(1)
c2.add_atribute(1, 2)
c3.add_atribute([(1, 2, 3, 3), (3, 1)])

c2.display()
c3.display()