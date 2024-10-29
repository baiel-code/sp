def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "True"
    return "False"

res = is_triangle(3, 6, 10)
print(res)


def is_lange(text):
    return True if len(text) > 3 else False
res = is_lange("baiel")
print(res)



def is_lange(text):
    return True if len(text) > 3 else False
d = input()
res = is_lange(text=d)
print(res)

def is_lange(text):
    return len(text) > 3
d = input()
res = is_lange(text=d)
print(res)
