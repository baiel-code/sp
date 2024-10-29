x = 10
a = not (x % 2 == 0 or x % 3 == 0)
print(a)
#10 % 2 = 0 == 0 == Trye or 10 % 3 = 0 == 0 == Trye,
# Trye, Trye, = Trye -not = False 
# 2 - тапшырма
b = not x % 2 == 0 or x % 3 == 0
print(b)
# 
# 3 - тапшырма
c = x % 2 != 0 or x % 3 == 0
print(c)
#  10  % 2 
# 4 - тапшырма 
d = x % 2 != 0 and x % 3 != 0
print(d)


