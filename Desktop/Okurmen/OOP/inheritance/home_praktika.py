class Age:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')

ag = Age('baiel',14,'male')
ag.info()

class Pro(Age):
    def __init__(self,name,age,gender,phone):
        super().__init__(name,age,gender)
        self.phone = phone
    def info(self):
        print(f'phone: {self.phone}')
p = Pro('baiel',14,'male','apple13')
p.info()
