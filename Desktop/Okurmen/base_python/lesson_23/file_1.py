import random
'''lst = [1,2,3,4,5]
print(random.randint(1,100))
print(random.random())
print(random.uniform(2.4, 2.5))
print(random.choice(lst))
random.shuffle(lst)
print(lst)
print(random.sample(lst,3))



a, b,c = map(int, input().split())
g = random.randint(a,b)
if g == c:
    print(True)
else:
    print(False)
print((a,b,c))
print(g)'''



names = ['baiel','bilal']
a = input()
n = random.choice(names)
print(n)

if names == a:
    print(True)
else:
    print(False)
print(names,a)


name = ['baiel','bilal']
r = random.choice(name)
print(r)
name = input('name: ')
print(r == name)



def get(a:int, b:int):
    return a / b
print(get(4,2))