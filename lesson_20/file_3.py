def get_count(func):
    count = 1
    def wrapper():
        nonlocal count 
        print(f'функся {func.__name__} {count} жолоу иштеди')
        func()
        count += 1
        print('kosh kelinis')
        
    return wrapper
@get_count
def hello():
    print("Салам!")
@get_count
def welcome():
    print('функся {func.__name__} {count} жолоу иштеди')
hello()
hello()
welcome()
welcome()
welcome()

