result = {}
numbers = [int(i) for i in input().split()]
for number in numbers:
    if number < 0:
        result[number] = "-"
    else:
        result[number] = "+"

print(result)