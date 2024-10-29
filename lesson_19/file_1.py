'''n = 100 
WID = 150
hir = 200


def fun(list):
    rec = "baiel"
    global WID
    WID = 250
    for i in list:
        print(i)
    print(rec)
    print(WID)

fun([1,2,3])
print(WID)
print(hir)
print(n)
print()

def fun1(n):
    print(n)
    def fun(m):
        print(m)
        nonlocal n 
        n = "baiel"
        print(n)
    fun("masele")
    print(n)
fun1('oku')'''


name = 'baiel'
def foi():
    global name 
    name = 'bai'

print(name)
foi()
print(name)
