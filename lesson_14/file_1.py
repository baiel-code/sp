# []
# {key: value, }

digits = {
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
    print(key, value)




my_dict = {i for i in input().split()}
res_dict = {}
for i in my_dict:
    key, value = i.split("=")
    res_dict[key] = value
print(res_dict)

res_dict = {}
for i in my_dict:
    key, value = i.split("=")
    if key == "house":
        print("Yes")
        break
    elif key == "True":
        print("Yes")
        break
    elif key == "5":
        print("Yes")
        break