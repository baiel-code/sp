cities = [city for city in input().split()]
for city in cities:
    if len(city) >= 5:
        print(city, end = ' ')
print()



# 2 тапшырма
numbers = [int(i) for i in input().split()]
result = []
for number in numbers:
    if number > 0:
        result.append("он")
    else:
        result.append("терс")
print(result)




#3 тапшырма
a = int(input("n: "))
for i in range(1, 11):
    print(f'{a} * {i} = {a * i}')
a = []
b = int(input())
for i in range(1,10+1):
    a.append(i*b)
print(a)
