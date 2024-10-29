print({f"{i}: {j}" for i, j in enumerate("baiel")})


list_gen = [int(i) for i in range(10)]
set_gen = {i for i in 'baiel'}
dict_gen = {f"{i}: {j}" for i, j in enumerate("baiel") }
print(dict_gen)