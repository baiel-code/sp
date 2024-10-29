class Per:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.name = name
        self.age = age
        self.gender = gender



    def __add__(self, other):
        return Per(self.name,self.age + other.age,self.gender)

    def info(self):
        print(f'Name: {self.name},\nAge: {self.age},\nGender: {self.gender}')



baiel = Per('baiel',14,'male')
nurlis = Per('nurlis',15,'Female')

res = baiel + nurlis
res.info()
