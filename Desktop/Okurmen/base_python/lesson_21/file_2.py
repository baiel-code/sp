'''file = open('lesson_21/usa.txt', 'a', encoding='utf-8')
file.write('baiel\n')
file.write('b\n')
file.writelines(['nurel\n','baiel\n'])
file.writelines(["bilal\n",'alinur\n'])
print(file.tell())
file.seek(0)
print(file.read())
file.writelines(['bilal\n'], 'baiel\n', 'nurlis\n', 'ali\n')
file.close
print(file.close)'''

'''try:
    a = 5
    b = 5
    c = a * b
    print(c)

except ZeroDivisionError:
    print('san 0 bolunboid')
except FileExistsError:
    print("file nor found error")
finally:
    print('finished')

try:
    a = int(input())
    p = input()
    b = int(input())
    if p == '*':
        print(a * b)
    if p == '//':
        print(a // b)
    if p == '-':
        print(a - b)
    if p == '+':
        print(a + b)
except ZeroDivisionError:
    print('san 0 bolunboit')
finally:
    print('finish')'''



file = open('lesson_21/usa.txt', 'a', encoding='utf-8')
file.write('\nbaiel\nis\ncoolll')

file = open('lesson_21/usa.txt', 'r', encoding='utf-8')
print(file.read)

file.close
print(file.close)