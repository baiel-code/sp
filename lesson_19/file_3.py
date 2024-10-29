'''def fun(name):
    def get_info():
        print(f'Welcome our team, {name}')
    return get_info

f = fun("Nurlis, kot")
f()

def get(age):
    def student(name):
        print(f"{name} you are studend")

    def shool(name):
        print(f"{name} you are shool  boy")
    

    if age > 18:
        return student
    return shool

person = get(age=14)
person("baiel")
'''


