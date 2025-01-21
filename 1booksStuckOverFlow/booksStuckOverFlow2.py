import heapq, sys
from array import array
import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


pr = factorial(4)
print(pr)


def unpacking(a, b, c, *args, **kwargs):
    print(a, b, c, args, kwargs)


unpacking(1, 2, 3)
unpacking(1, 2, 3, 4)


def func3(mylist):
    for item in mylist:
        print(item)


func3([1, 3, 4, 5, 6])

s = lambda x: x * x
a = s(2)
print(a)

name_lenght = map(len, ['German', 'Yana'])
print(list(name_lenght))

arr = [1, 2, 3, 4, 5, 6, 7]
ads = [i for i in filter(lambda x: x % 2 == 0, range(8))]
print(ads)

def raise_power(x,y):
    return x**y
print(raise_power(x=2,y=2))

def super_secret_func(f):
    return f

@super_secret_func
def my_function():
    print("This is my function secret")

my_function()
re = my_function()
print(re)

def print_args(func):
    def inner_func(*args, **kwargs):
        inner_func.count += 1
        print(f'вызов функии {func.__name__} { inner_func.count}')
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    inner_func.count = 0
    return inner_func

@print_args
def multiplay(num_a, num_b):
    return num_a * num_b

print(multiplay(3,5))
print(multiplay(3,5))

# Подсчет вызовов функции
def count_calls(func):
    """Декоратор для подсчёта вызовов функции"""
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1  # Увеличиваем счётчик вызовов
        print(f"Вызов функции '{func.__name__}' номер {wrapper.call_count}")
        print(kwargs)
        print(args)
        return func(*args, **kwargs)
    wrapper.call_count = 0  # Инициализация счётчика вызовов

    return wrapper

@count_calls
def example_function(x, y):
    return x + y

# Тестируем
print(example_function(1, 2))
print(example_function(3, 4))
print(example_function(5, 6))


def func2(func):
    def wrapper(*args, **kwargs):
        wrapper.count +=1
        print(args)
        print(kwargs)
        print(f'вызов функции {func.__name__} - {wrapper.count}')
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@func2
def multi(a,b):
    return a * b
multi(1,2)
multi(1,2)
multi(1,2)


def podcet_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time_ns()
        f = func(*args, **kwargs)
        t2 = time.time_ns()
        print(f'функция {func.__name__} затрачено времени { t1 - t2}')
        return f
    return wrapper

@podcet_time
def example_time():
    return None

example_time()