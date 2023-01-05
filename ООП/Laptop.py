class Laptop:
    def __init__(self, brand, model, price, laptop_name=''):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'

laptop1 = Laptop('dell', 'N500', 33000)
laptop2 = Laptop('dell', 'N800', 52500)
