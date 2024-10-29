f = lambda n: "он сан" if n > 0 else "терс"
print(f(-5))


def g(n):
    if n == 0:
        return 0
    g(n-1)
    print(n)

g(8)


got = lambda n: n ** 2
print(got(9))


get = lambda n, m: n / m if m != 0 else None
print(get(10,0))
