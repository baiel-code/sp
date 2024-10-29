'''
a = int(input())
b = input()
c = int(input())
def k(a,b,c):
    if b == '*':
        print(a*c)
    elif b == '/':
        print(a/c)
    if b == '+':
        print(a+c)
    elif b == '-':
        print(a-c)
k(a,b,c)



def b(n):
    j = []
    t = []
    for i in range(1, n +1):
        if i % 2 ==0:
            j.append(i)
        else:    
            t.append(i)
    print(j)
    print(t)
b(20)



def n(b):
    m = []
    h = []
    for i in range(1, b +1):
        if i % 2 == 0:
            m.append(i)
        else:
            h.append(i)
    print(m)
    print(h)
n(30)'''


"""
def get_sum(a, b, c, is_verboose=True):
    if is_verboose:
        print(f'a = {a},  b = {b}, c = {c}')
    return a + b + c

res = get_sum(2, 4, 5, is_verboose=False)
print(res)




def fun(*args, **kwargs):
    print(args, kwargs)

fun(1,2,3,4,5)
fun(name=f"Nurlis{12+4}", age=22, gender="male")
fun(1,2,3,4,5, name="Arsen", age=19, gender="male")
fun()
"""



def fon(*args, **kwargs):
    print(args,kwargs)
fon(1,2,3,4,'baiel',h='jjk',k=789)
fon(1,2,3,4, name='baiel', age=14,)
fon(...)



