class Counter:
    def start_from(self, start = 0):
        self.start = start
        return self.start

    def increment(self):
        self.start +=1
        return self.start


    def display(self):
        print(f"Текущее значение счетчика = {self.start}")

    def reset(self):
        self.start = 0
        return self.start


c1 = Counter()
c1.start_from()
c1.increment()
c1.display() # печатает "Текущее значение счетчика = 1"
c1.increment()
c1.display() # печатает "Текущее значение счетчика = 2"
c1.reset()
c1.display() # печатает "Текущее значение счетчика = 0"

c2 = Counter()
c2.start_from(3)
c2.display() # печатает "Текущее значение счетчика = 3"
c2.increment()
c2.display() # печатает "Текущее значение счетчика = 4"
