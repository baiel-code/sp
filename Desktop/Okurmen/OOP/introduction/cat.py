class Cat:
    print('создайте себе кошку')
    def __init__(self):
        a = input('имя вашего кота: ')
        b = int(input('укажите возрозть ващего кота: '))
        c = input('пол вашего кот: ')
        d = input('свет вашего кота: ')
        self.name = a
        self.age = b
        self.gender = c
        self.color = d
    def info(self):
        print('ваш кот\n','$' * 20)
        print(f'имя кота: {self.name}')
        print(f'возрость вашего кота: {self.age}')
        print(f'пол вашего ката: {self.gender}')
        print(f'свет вашего ката: {self.color}')
ob = Cat()
ob.info()