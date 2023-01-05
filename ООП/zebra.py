class Zebra:
    count = 0
    def which_stripe(self):

        if self.count % 2 == 0:
            print("Полоска белая")
            self.count += 1
        else:
            print("Полоска черная")
            self.count += 1


z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()

z2 = Zebra()
z2.which_stripe()
z2.which_stripe()


