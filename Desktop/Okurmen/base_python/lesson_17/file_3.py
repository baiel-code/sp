def get(v1, v2):
    print("value", v1)
    print("value", v2)
    

a = 4 
b = 3 
get(b, a)
get(v1= b, v2=a)
get(v1= "bishkek", v2= "london")
get("bishkek", v2= "london")
get("kil","ko")
get(v2="osh", v1="bishkek")


def get(a, b, c = 5):
    print(a + b + c)
    print()

get(a=2, b=5)
get(a=3, b=4, c=2)

def get_list(n=[]):
    print(f"n:" "okurmen")
a = [1, 2, True, "oekurmen"]

get_list()
get_list(n=a)

def get_dick(people):
    for name, sun in people.items():
        print(name,sun)
b = {
    "baiel": "14"
}
get_dick(b)

def get_set(un):
    print("un: ", un)


c = {1,2,3,1,2,3,1,2,3,"baiel","baiel",True,True}
get_set(un=c)

def get_sum(nums):
    totol_sum = 0
    for num in nums:
        totol_sum += num
    print(f"tol = {totol_sum}")

d = [1,2,3,4,5]
get_sum(nums=d)



def get_sum(nums):
    totol_sum = 1
    for num in nums:
        totol_sum *= num
    print(f"tol = {totol_sum}")

d = [1,2,3,4,5]
get_sum(nums=d)

def get_sum(a, b):
    print(a + b)
    return a+b
s = get_sum(5, 6)
print(s)

def get_a(w, h):
    return w * h 
a = get_a(5, 6)
print(a)

def get_sum(n):
    t = 1
    for nu in n:
        t *= nu
    return t

res = get_sum([100, 200, 300])
print(res)



    
