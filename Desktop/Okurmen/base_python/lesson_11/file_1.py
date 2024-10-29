n = 23
m = 35
if n > m:
    k = n 
else:
    k = m 
print("simple if: ",k)
k = n if n > m else m
print("ternarnyi if ",k)
print("san" if input("slovo").isdigit() else "tamga")


