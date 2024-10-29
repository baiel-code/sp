s = 0 
while True:
    n = int(input("N: "))
     
    if n == 0:
        break
    elif n < 0:
        continue
    else:
        s += n 
print(f"сумма = {s}")

n = int(input("n"))
i = 1
while n > i ** 2: 
    i += 1
print(i)