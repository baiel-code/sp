a = True
i = 0 
while a:
    i = i + 1
    if i > 5:
        a = False
 

print(i)
print(a)
n = int(input("n: "))
while n > 0:
    print(n)
    n = n -1 
    
n =int(input("n: "))
i = 1 
s = 0 
while i <= n:
    s += i
    i += 1
print(s)
m = int(input("m; "))
i = 1 
s = 1
while i <= m:
    s *= i
    i += 1
    
print(s)

n = int(input("n :"))
m = int(input("m :"))
s = 0
t = 1
while n <= m:
    s += n
    t *= n
    n += 1
print(s)
print(t)


n = int(input("n; "))
i = 0 
s = 0 
while i <= n:
    i += 1 
    print(i)
    if i == 5:
        break
    s += i 
print(s)
for i in range(n):
    if i % 2 == 1:
        continue
    print(i)




s = -0 
while True:
    n = int(input(""))
    if n == 0:
        break


    s += n 
    print(f"общая сума = {s}") 
