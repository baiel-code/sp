class Bim:
    def __init__(self):
        a = input('Name: ')
        b = input('Surname: ')
        c = int(input('Age: '))
        d = float(input("Height: "))
        i = int(input('Weight: '))
        self.name = a
        self.surname = b
        self.age = c
        self.height = d
        self.weight = i


    def bm(self):
        return self.weight / self.height ** 2

    def check(self):
        bmi = self.bm()
        if bmi <= 18.5:
            print('худой')
        elif 18.5 < bmi <= 25:
            print('нормално')
        elif 25 < bmi <= 29.9:
            print('Избыточный вес')

        else:
            print('Ожирение')

    def info(self):
        print('#' * 10)
        print('BMI')
        print(f'Name:  {self.name} {self.surname}')
        print(f'age: {self.age}')
        print(f'height: {self.height}')
        print(f'weight: {self.weight}')

ob = Bim()
ob.info()
ob.check()
