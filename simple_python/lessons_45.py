# Декораторы функций
def func_decorator(func):
    def wrpapper(*args, **kwargs):
        print("---------------------- how -----------------")
        func(*args, **kwargs)
        print("---------------------- how -----------------")
    return wrpapper

def some_func(title):
    print("Void some func "+ title)

f = func_decorator(some_func)
some_func("Python")