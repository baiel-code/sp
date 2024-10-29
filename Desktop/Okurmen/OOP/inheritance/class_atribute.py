class Product:
    company = 'ATA'

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(selfs):
        print(f'Name: {selfs.name}')
        print(f'Price: {selfs.price}')


product_1 = Product('Aplee', 100)
product_2 = Product('Banana', 200)
print(product_1.name)
print(product_1.price)
print(product_1.company)

Product.company = 'shoro'
print(product_1.company)

print(product_2.name)
print(product_2.price)
print(product_2.company)


class Pro:
    com = 10
    gmail = 20

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name)
        print(self.age)


pro_1 = Pro('baiel', 14)
pro_2 = Pro('nurlis', 'kot')
print(pro_1.name)
print(pro_1.age)

print(Pro.com)
print(Pro.gmail)
