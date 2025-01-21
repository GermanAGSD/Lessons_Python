import heapq, sys
from array import array
from functools import partial
from operator import mul
import operator

t = {x for x in range(10) if x % 2 == 0}
print(list(t))

filtered = filter(lambda x: x % 2 == 0, range(10))
print(list(filtered))

res2 = map(lambda x: 2 * x, range(10))
print(f'res2 = {list(res2)}')

mp = map(lambda x: x % 2, range(10))
print(f'mp = {list(mp)}')

mapa = map(abs, (1, -1, 2, -3, -4))
print(list(mapa))

mp = map(float, range(10))
print(type(mp))

rate = 0.9
dollar = {
    'under_my_bed': 1000,
    'jeans': 45,
    'bank': 5000
}
print(sum(map(partial(mul, rate), dollar.values())))
print(sum(map(lambda x: rate * x, dollar.values())))

# Вычислить разницу между
measurement1 = [100, 111]
measurement2 = [102, 117]

mes = map(operator.sub, measurement1, measurement2)
print(list(mes))

insect = ['fly', 'ant', 'beetle', 'cankeworm']
f = lambda x: x + ' is an'
sad = map(f, insect)
print(list(sad))

# 1 sp
z = [x + y for x, y in [(1, 2), (3, 4), (5, 6)]]
print(z)
# Аналогично
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x + y)

af = sum(1 for x in range(1000) if x % 2 == 0 and '9' in str(x))
print(af)

items = ['1', '2', '3', '4']
ag = map(float, items)
print(list(ag))

ax = list(filter(None, [1, 0, 2, [], 'a']))
print(ax)

number = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nlargest(4, number))
print(heapq.nsmallest(4, number))

people = [
    {'firstname': 'John', 'lastname': 'Doe', 'age': 30},
    {'firstname': 'Jane', 'lastname': 'Smith', 'age': 25},
    {'firstname': 'Emily', 'lastname': 'Johnson', 'age': 35}
]

oldest = heapq.nlargest(2, people, key=lambda person: person['age'])
print(oldest)

number2 = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]

heapq.heapify(number2)
print(number2)

af = tuple('tuple')
print(af)

io = ('a',)
print(type(io))
print(io)
print(len(io))
po = (1, 2, 3,)
for k, y in enumerate(po):
    print(k, y)

print(sys.getrecursionlimit())

asq = [1, 2, 3, 4]
asq.insert(1, 5)
print(asq)
asq.pop(1)
print(asq)

myarray = array('i', [1, 2, 3, 4])
print(myarray)
myarray.insert(0, 3)
print(myarray)
myarray.pop(1)
print(myarray)
myarray.remove(3)
print(myarray)
for x, y in enumerate(myarray):
    print(x, y)


def func(**kwargs):
    # for name, value in enumerate(kwargs):
    for name, value in kwargs.items():
        print(name, value)


func(value1=1, value2=2, value3=3)

foo = {
    '1': 'one',
    '2': 'two'
}

func(**foo)

greet_me = lambda: 'hello'
print(greet_me())

strip_and_upper = lambda s: s.strip().upper()
r = strip_and_upper(" hello ")
print(r)

greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting('hello', 'world', world='world')

re = sorted(['foo', ' bAR', 'BAZ'], key=lambda s: s.strip().upper())
print(re)

my_list = [3, -4, -2, 5, 1, 7]
rt = sorted(my_list, key=lambda x: abs(x))
print(rt)

ry = list(map(lambda x: abs(x), my_list))
print(ry)


def appendin(elem, to=[]):
    to.append(elem)
    return to


print(appendin(3))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


pr = factorial(4)
print(pr)


def unpacking(a, b, c, *args, **kwargs):
    print(a, b, c, args, kwargs)


# unpacking(1,2)
unpacking(1, 2, 3, 4)


def func3(mylist):
    for item in mylist:
        print(item)


func3([1, 3, 4, 5, 6])
