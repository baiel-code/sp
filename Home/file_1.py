                               # lesson_1
"""print("my name baiel")
print(7+8)
print(9+9)
print((3-5) + (4 +9)/2 )
print("#568")
                               # lesson_2
print("baiel",end= " ")
pri nt("many")
print("baiel", "osh", end=" " )
print("bishkek")   
i = input("name: ")
p = input("surname: ")
o = input("age: ")
print("welcome",p,i,"vam",o,"let")
x = 12
a = not(x / 3 == 0 or x*2 == 24)
print(a)
j = 40 
k = (j / 2 == 20 or j / 4 == 9)
print(k)
w = "pop"
u = "pop-1"
print(w + " " + u + " " + w + " " + "lo") 
s = "50"
print(w +" "+ s)
iy = "baiel"
print(len(iy))
citi = 'kurgustan'
citi1 = 'kurg'
print(citi in citi1)
city = input("ведите; ")
citu1 = input("ведите; ")
print(city in citu1)
print(ord("a"))
print(len("pyton is not fan"))
baiel = input("велите слово :")


print(baiel[0])
print(baiel[1])
print(baiel[2])
print(baiel[3])
print(baiel[4])
baiel_1 = input("аедите слова")
print(baiel_1[0],baiel_1[-1])
baiel_2 = input("slova ")
print(baiel_2[::-1])
print(baiel_1 > baiel_2)
print(ord("2"))
print(ord("1"))
#String.upper(увеличиваеть слова)
# String.lower(уменшаеть слова)
# String.find(для нашождение слов)
# String.index()
# String.count()
# String.strip()
# String.rstrip()
# String.lstrip()
# String.replace()
# String.isalpha()
# String.Stringgit()
baiel_3 = input("ведите слова для увиличение: ")
baiel_4 = baiel_3.upper()
print(baiel_4)
baiel_5 =  input("ведите слова для уменшение: ")
baiel_6 = baiel_5.lower()
print(baiel_6)
baiel_7 = input("ведите слова: ")
baiel_8 = baiel_7.find("on")
print(baiel_8)
baiel_9 = input("ведите слово: ")
baiel_10 = baiel_9.count("ba")
print(baiel_10)
baiel_11 = "    baiel    "
baiel_12 = baiel_11.rstrip()
print(baiel_12)
baiel_13 = baiel_11.lstrip()""""""
n = int(input("n"))
for o in range(n):
    print(f"{o}baiel")
m = int(input())
n = input()
for k in range(m):
    print(f"{k}{n}")""""""""
citis = ["bishkek", "osh","poxui"]
numbers = [1,5,6,7]
name = input("ведите свой имя :")
for citi in citis:
    print(citi)
for number in numbers:
    print(number)
for name_1 in name:
    print(name_1)
m = input("ведите слово: ")
for index, slovo in enumerate(m):
    print(f'{index} {slovo}')
a = 4
b = 5 
   

for i in range(a):
    for i in range(b):
        print(f"f = {i}, i = {i}")"""'''
n_texst = input(" :")
print(n_texst)
n = [int(i) for i in n_texst.split("-")]
sum_nuber = 0 
for nuber in n:
    sum_nuber += nuber
print(n)
print(sum_nuber)
n_texst = input(" :")
print(n_texst)




























f = input("ведите своё имя ")
h = int(input("ведите саой возрост "))
if h <= 18:
    print("вам нелзы")
else:
    print(f"welcome {f} вам можено так как вам {h}")''''''



cities = ["Bishkek","Astana","osh","Stambul"]
print(cities)
cities[2] = "Talas"
print(cities)
cities[-2] = "Frunze"
print(cities)
print(cities[1:3:2])'''
'''
names = ["baiel", "nurlis", "bilal", "daniel", "i"]
print(names)
names[4] = "timur"
print(names)
print(names[1:3:2])
names.append("num")
print(names)
names.extend(['kil'])
print(names)
names.insert(0, "bai")
print(names)
names.pop(3)
print(names)
names = ["Arsen", "Timur", "Bilal", "Baiel","Nurlis", "Daniel", "Alinur"]
l = len(names)
names.pop(l//3)
print(names)''''''

msg = [1, 2, 3, [9, 6, 4], True, "Okurmen", ["Bishkek", "narun"]]
print(msg[0])
print(msg[6][1])
print(msg[3][0] + msg[3][1] + msg[3][2])


print("int" if input().isdigit() else "float")''''''


g = input()
b = int(input())
for a in range(b):
    print(f'{a} {g}')



k = input("имя")
p = input("фамиля")

def s(k, p):
    print(f'урмату {p} {k} сиз програманы тура кылдыныз')


s(k, p)

'''





'''digits = {
    "one": 1,
    "two": 2,
    "three": 3,
}

(digits.get("four"))
digits["four"] = 5 
digits["four"] = 4 
print(digits.get("five"))
print(digits)
print(digits.keys())
print(digits.values())

for key, value in digits.items():
    print(key, value)''''''

d = {
    "g": 1,
    "f": 2,
    "s": 3,
}

print(d.get('four'))
d["four"] = 4
print(d)'''













                                          #def

'''
def ps():
    print("baiel")
ps()


def ol():
    n = [1,23,4,4,5,]
    l = 0
    for f in n:
        l += f 
    print(l)



ol()

def i():
    print("b\ne")
i()



def l(n):
    ns = 1
    for i in range(1, n+1):
        ns *= i 
    print(ns)

l(5)

def k(a, b):
    print(a + b)

k(4, 5)'''
import random

def