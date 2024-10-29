class Person:
    def __init__(self,name,sername,age):
        self.name = name
        self.sername = sername
        self.age = age


    def info(self):

        print(f"Name is {self.name}\nSername is {self.sername}\nage is {self.age}")

class Person_1(Person):
    def __init__(self,name,sername,age,work):
        super().__init__(name,sername,age)
        self.work = work

    def info(self):
        print(f'work is {self.work}')
per = Person('baiel','ergeshov',14)
per.info()

perr = Person_1('baiel','ergeshov',14,'boss')
perr.info()
