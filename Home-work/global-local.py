w = 100 
n = 150 
k = 200
def fun(lst):
    def fun1(m):
        print(m)
        nonlocal n 
        n == 'bairel'
    global w
    w = 300
    rec = 'baiel'
    for i in rec:
        print(i)
    print(w)
    print(rec)

fun([1,2,3])
print(w)
print(n)
print(k)

