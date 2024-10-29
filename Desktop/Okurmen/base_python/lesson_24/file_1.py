import random
'''
def get():
    return random.randint(1,10)
def chek(comp, pern):
    return comp == pern
def main():
    s = 0
    comp_num = get()
    while True and s < 3:
        person = int(input('ведите одно число: '))
        if chek(comp_num, person):
            print('siz tura taptiz')
            break
        else:
            print('siz tura emes taptiz')
            s += 1
    else:
        print(f'comp {comp_num} degen')
main()'''
a = int(input('началный диопозон": '))
b = int(input('конец диопозона: '))


def got():
    return random.randint(a,b)


def cok(com, per):
    return com == per
def man():
    c = 0
    comp_number = got()
    while True and c < 3:
        chel = int(input('ведите одно чмсло: '))
        if cok(comp_number,chel):
            print('вы угадали :')
            break
        else:
            print('вы не угадали попробуйе ещё раз: ')
            c += 1
    else:
        print(f'вы не угадали компютер загадал {got()} :')
man()

