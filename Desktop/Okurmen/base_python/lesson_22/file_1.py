a = [int(i) for i in range(10)]
b = (i for i in range(10))
print(next(b))
print(next(a))


def fun(x):
    return int(x) > 0

a = map(fun,input().split(0))
print(list(a))

n = [1,2,3,4,5]
b = map(lambda x: x % 2 == 0, n)
print(list(b))


cities = ["Bishkek", "London", "Paris", "Madrid", "Berlin"]
a = filter(lambda x: x[-1] == "k", cities)
print(a) 
print(list(a))

def is_prime(n):
    for i in range(2, int(n **0.5) +1 ):
        if n % i == 0:
            return False
    return True
numbers = [5, 3, 6, 7, 11, 15]
a = filter(is_prime, numbers)
print(list(a))



a = [1,2,3,4,5]
b = ['pne', 'two', 'three', 'four']
d = [6,5,4,3,2,1]
c = zip(a,b,d)
print(list(c))

a = [1,2,3,4,5]
b = ['pne', 'two', 'three', 'four']
c = zip(a,b)
print(dict(c))

def fun(numbers):
    for i in numbers:
        yield i 
numbers =  [ 1,2,3,4,5]
a = fun(numbers=numbers)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

def get_(n):
    return n // 2 * 2+2
print(get_(5))

def get(num):
    for i in num:
        if i % 2 == 0:
            yield i


numbere = [1,2,3,4,5]
a = get(numbere)
