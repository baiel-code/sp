def fibbonaci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibbonaci(n - 1) + fibbonaci(n - 2)
res = fibbonaci(5)
print(res)


def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)


res = f(2)
print(res)
