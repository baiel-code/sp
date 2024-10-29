try:
    citi = [cyty + "\n" for cyty in input ().split()]
    with open('lesson_21/cites.txt', 'a', encoding='utf-8') as file:
        file.writelines(citi)

except FileNotFoundError:
    print('myndai fail jok')

finally:
    print('finished')



try:
    with open('lesson_21/cites.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

except FileNotFoundError:
    print('myndai fail jok')

finally:
    print('finished')


