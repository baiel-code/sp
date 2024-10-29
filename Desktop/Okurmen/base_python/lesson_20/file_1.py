# декаратор 
def get_info(fonc):
    def waper():
        print('start')
        fonc()
        print("finish")
    return waper
@get_info

def fun():
    print('baiel')
fun()



def get(f):
    def wapr():
        print('kot')
        f()
        print('al')
    return wapr
@get

def fu():
    print('nurlis')
fu()

def dot(o):
    def wor():
        print()
        o()
        
