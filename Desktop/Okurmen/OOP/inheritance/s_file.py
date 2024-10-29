class Spek:
    def __init__(self,name,surname,age,gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def info(self):
        print(f'Name: {self.name}')
        print(f'Surname: {self.surname}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')

s = Spek('Baiel','ergeshov',14,'male')
s.info()

class Prak(Spek):
    def __init__(self,name,surname,age,gender,phone):
        super().__init__(name,surname,age,gender)
        self.phone = phone
    def info(self):
        print(f'phone {self.phone}')
pr = Spek('baiel','ergeshov',14,'male',)


prr = Prak('baiel','ergeshov',14,'male','redmi_7A')
prr.info()



class Baiel:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f'Name: {self.name}')
        print(f'age: {self.age}')
b = Baiel('baiel',14)


class Nurel(Baiel):
    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self.gender = gender
    def info(self):
        print(f"Gender: {self.gender}")
n = Nurel('nurel',14,'male')



class Ex(Nurel):
    def __init__(self,name,age,gender,rost):
        super().__init__(name,age,gender)
        self.rost = rost
    def info(self):
        print(f'Rost: {self.rost}')
r = Ex('baiel',14,'male',160)
r.info()