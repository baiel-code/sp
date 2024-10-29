def fun_1(a, b, c): # фактические параметры
    pass

def fun_2(name="Okurmen", age=18): # формальные параметры
    pass


fun_1(1, 2, 3) # порядковые аргуметы
fun_1(b=1, c=2, a=3) # именованные аргуметы
fun_2(name="Arsen", age=22) # именованные аргуметы


def get_sum(a, b, c, is_verboose=True):
    if is_verboose:
        print(f'a = {a},  b = {b}, c = {c}')
    return a + b + c

res = get_sum(2, 4, 5, is_verboose=False)
print(res)




def get_sum(*args):
    sum_all = 0
    print(args)
    for i in args:
        sum_all += i
    return sum_all

res = get_sum(1,3,2)
print(res)


def get_sum(*args):
    sum_all = 1
    print(args)
    for i in args:
        sum_all *= i
    return sum_all

res = get_sum(1,3,2)
print(res)





def info(**kiwargs):
    print(kiwargs)

info(a=2, b=3, c=1)



def info(**kwargs):
    print(kwargs)

info(a=2, b=1, c=3, d=6, e=5)

def fun(*args, **kwargs):
    print(args, kwargs)

fun(1,2,3,4,5)
fun(name=f"Nurlis{12+4}", age=22, gender="male")
fun(1,2,3,4,5, name="Arsen", age=19, gender="male")
fun()

def fon(*args,**kwargs):
    for i in args:
        print(i, end=" ")
    print()
    for key, vay in kwargs.items():
        print(key, vay)

fon(1,2,3,4,5,citi="baiel", n="gl")


def fi(*args):
    sum = 0 
    print(args)
    for i in args:
        sum += i
    return sum
res = fi(4,6,5,3,2,1)
print(res)


def g(*args):
    su = 0
    print(args)
    for i in args:
        su += i
    return su 
r = g(1,3,4,5,2)
print(r)


n = int(input())
b = int(input())
def s(n,b):
    print(n,b)
    for i in n,b:
        p = n*b

    return p
r = s(n,b)
print(r)

