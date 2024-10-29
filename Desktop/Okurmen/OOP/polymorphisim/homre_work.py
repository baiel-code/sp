'''class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print(f'Name: {self.name} Price: {self.price}')
        print(f'Name: {samsung.name} Price: {samsung.price}')


    def __add__(self, other):
        return Product(self.name, self.price + other.price)



apple = Product('apple_15pro',1000)
samsung = Product('samsung_s24',1000)
apple.info()
res = apple.price + samsung.price
print('total amount',res)
'''


class Pr:
    def __init__(self,name,price):
        self.name = name
        self.price = price


    def info(self):
        print(f'Name: {self.name}')
        print(f'Price: {self.price}')

    def __add__(self, other):
        return Pr(self.name,self.price + other.price)

pr1 = Pr('banana',150)
pr2 = Pr('apple',100)
pr1.info()
pr2.info()
res = pr1.price + pr2.price
print(res)
