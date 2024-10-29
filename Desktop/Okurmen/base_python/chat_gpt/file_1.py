def k():
    numbers = [1,2,3,4,5]
    a = 1
    for i in numbers:
        a *= i
    print(a)
#k()

s = ('helo')
#print(s[-1::-1])


n = [111111111,99]

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


sum_digits = [sum_of_digits(num) for num in n]

max_sum = max(sum_digits)


print(f"Сумма цифр чисел: {sum_digits}")
print(f"Большее из сумм цифр: {max_sum}")


def n():
    n = 5
    for i in n:
        i[-1] + i[0]
        print(i)
n()
