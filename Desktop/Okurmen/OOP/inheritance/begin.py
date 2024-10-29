class Animal:
    def __init__(self, breed, age,name):
        self.breed = breed
        self.age = age
        self.name = name

    def info(self):
        print(f'Breed is {self.breed}\nAge is {self.age}')

class Dog(Animal):
    pass

dog_1 = Dog('haski',3,'bob')
dog_1.info()
print(':' * 30)
class Person:
    def __init__(self,name,sername):
        self.name = name
        self.sername = sername


    def info(self):

        print(f"Name is {self.name}\nSername is {self.sername}")

class Person_1(Person):
    def __init__(self,name,sername,work):
        super().__init__(name,sername)
        self.work = work

    def info(self):
        print(f'work is {self.work}')
per = Person('baiel','ergeshov')
per.info()

perr = Person_1('baiel','ergeshov','boss')
perr.info()

