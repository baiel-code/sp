class Anketa:
    def __init__(self, name, like_food, hobby, like_sport=""):
        self.name = name
        self.like_food = like_food
        self.hobby = hobby
        self.like_sport = like_sport

    def info(self):
        print(f'Name: {self.name}')
        print(f'Like food: {self.like_food}')
        print(f'Hobby: {self.hobby}')
        print(f'Like sport: {self.like_sport}')
        print('#' * 20)

ob_1 = Anketa('Baiel', 'kuurdak', 'Watch TV', 'play')
ob_2 = Anketa('Bilal', 'oromo', 'Play', 'Soccer')
ob_3 = Anketa('Alinur', 'Mant', 'slip', 'volleyball')
ob_4 = Anketa('Nurlis', 'Pelmen', 'swim', )

ob_1.info()
ob_2.info()
ob_3.info()
ob_4.info()

