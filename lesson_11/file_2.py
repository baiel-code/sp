k = input()
a = input()
n = int(input("N :"))
for a in range(n):
    print(f"{a} {k}")
a = int(input())
b = input("b: ")
for k in range(a):
    print(f"{k}{b}")
a = int(input())
d = 1
for i in range(1, a + 1):
    d = d * i
print(d)
n = int(input("n "))
m = int(input("m "))
s = 0
t = 1
for d in range( n, m +1):
    s = s + d
    t = t * d
print(s)
print(t)