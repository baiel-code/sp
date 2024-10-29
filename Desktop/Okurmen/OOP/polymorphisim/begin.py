class Person:


    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def __add__(self, other):
        return Person(self.name,other.name, self.age + other.age)
        #return Person(self.name, self.age + self.age, self.gender)


    def info(self):
        print(f'Name: {self.name}\nName: {self.name}\nAge: {self.age}')





asan = Person('Asan', 21, 'female')
uson = Person('Uson', 30, 'Male')


res = asan + uson
res.info()
