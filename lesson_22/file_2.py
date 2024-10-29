a,b,n= map(int,input().split())

if a < 0:
    c = abs(a)
    print(c)
else:
    print(a)
if b < 0:
    c = abs(b)
    print(c)
else:
    print(b)
if n < 0:
    c = abs(n)
    print(c)
else:
    print(n)


def a(i):
    t = map(lambda p: tuple(p.split('=')), i)
    return list(t)
i = "key_1=value_1 key_2=value_2 key_3=value_3".split()
r = a(i)
print(r)




def ia(n):
    return 10 <= n <= 99 or -99 <= n <= -10

i= (map(int, input().split()))

t = list(filter(ia, i))

print(" ".join(map(str, t)))


