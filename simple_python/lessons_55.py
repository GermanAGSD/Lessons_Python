# Выражение генератора
def get_list():
    for x in [1,2,3,4]:
        yield x

a = get_list()
print(next(a))