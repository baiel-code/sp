'''data  = {
    "ienovo": 2024,
    "dell": 2020,
    "hp": 2019,
}

m = input()
n = int(input())
data[m] = n 
print(data)'''''''
  

ba = {}
name = input()
yers = int(input())
a = "kid"
b = "adit"
c = "man"
if yers < 12:
    ba[name] = a
elif yers > 18:
    ba[name] = b
elif yers <= 18:
    ba[name] = c
print(ba)'''
data = {
    "Arsen": 22,
    "Timur": 19,
    "Aibarchyn": 19,
    "Jurgal": 15,
    "Malika": 15,
    "Bilal": 15,
    "Daniel": 15,
    "Baiel": 15,
    "Nurlis": 15,
}
for i,y in  data.items():
    if y < 12:
        data[i] = "kid"
    elif 12 <= y <18:
        data[i] = "aduld"
    else:
        data[i] = "man"
    
print('\n\n')
for key, value in data.items():
    print(key,value)