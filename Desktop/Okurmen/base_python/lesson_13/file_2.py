n = 4 
m = 5 


for i in  range(n):
    for j in range(m):
        print(f'i = {i}, j = {j}')
names = ["Nurlis", "baiel", "timur", "daniel", "bilal"]
fa = [1,2,3,4,5,6]
b = []
for i in n:
    b.append(i**2)
print(b)

c = [i**2 for i in n]
print(c)
citys  = ["bishkek", "talas", "osh"]
city_upper= [cities.upper() for cities in citys]
city_lower = [cities.lower() for cities in citys]
print(city_upper)
print(city_lower)
n_texst = input(" :")
print(n_texst)
n = [int(i) for i in n_texst.split(",")]
sum_nuber = 0 
for nuber in n:
    sum_nuber += nuber
print(n)
print(sum_nuber)
n_texst = input(" :")
print(n_texst)


n = [int(i) for i in n_texst.split(",")]
sum_nuber = 1
for nuber in n:
    sum_nuber *= nuber
print(n)
print(sum_nuber)


b = input()
a = [len(i) for i in b.split(" ")]
print(a)
b = input()
a = [f" {b}: {len(i)}"for i in b.split(" ")]
print(a)
