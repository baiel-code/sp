import random
a = input('напишете горады: ').split()
b = random.choice(a)

print('Python выбираеть: ',b)

a = input('напишите имена студентов: ').split()
b = random.sample(a,3)
print('Pyton выбираеть',b)