'''from pprint import pprint
import time
from math import pi, sin, ceil  as cl

def ceil(x):
    print("our ceil")
    return x



print(sin(1))
print(ceil(5.1))
print(cl(5.2))
#pprint.pprint(locals())
pprint(time.daylight)



with open("lesson_21/usa.txt","a",encoding="utf-8") as file:
    a = input()
if a == ' ':
    a,'\n'
file.write(a)'''

a = [int(i) for i in range(10)]
b = (i for i in range(10))
print(next(b))
print(next(a))