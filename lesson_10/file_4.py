x =  4 
if x < 0:
    x = -x 
    print(x)
else:
    print("print")
print(x)
# bool (true, folse)
# str("")
# int (-n ..., -2, -1, 0, 1, 0, 1, 2, 3, ....n )
 # float(4.5, 5.5, 9.0, )
 
print(type(-2))
print(type(-3.44))
print(type("5948"))
print(type(True))
n = input("ведите чисдо")
m = int(n)
n = int(input("ведите чисдо"))
print(type(m))
n = input('ведите число')
if n.isdigit():
    n = int(n)
else:
    print("san jaziniz")
print(type(n))
o = int(input("ведите число: "))
p = int(input("ведите число: "))
if o < p:
    print(o)
else:
    print(p)
o = (input("ведите число: "))
p = (input("ведите число: "))
if o == p:
    print("==")
else:
    print("-")
i = int(input("ведите минуту"))
n = i % 5 
if 1 <= n  <= 3:
    print("grin")
else:
    print("red")


    




