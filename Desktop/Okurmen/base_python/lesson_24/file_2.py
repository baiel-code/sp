import random
a = int(input('ведите началный диопозон: '))
b = int(input('ведите конец диопозон: '))
def got():
    return random.randint(a,b)

def pri(python, person):
    return python == person

def oll():
    s = 0
    python_number = got()
    while True and s < 3:
        chelovek = int(input('угадайте число pythona :'))
        if pri(python_number,chelovek):
            print('вы выйграли')
            break
        else:
            print('вы не угадали попробуйте ещё раз ')
            s += 1
    else:
        print(f'к сожелению вы проиграли Pathon загадал число {python_number}')
oll()
