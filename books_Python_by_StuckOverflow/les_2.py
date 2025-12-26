from array import array

for i in (0, 1, 2, 3, 4):
    print(i)
    if i == 2:
        print("Breaking Loop")
        break

for a in (0, 1, 2, 3, 4, 5):
    if a == 2 or a == 4:
        print("Continue")
        continue
    print(a)

for index, items in enumerate(["one", "two", "three", "four"]):
    print(index, '::', items)

d = {"a": 1, 'b': 2, 'c': 3}

for key in d.keys():
    print(key)

for val in d.values():
    print(val)

print(d.items())

for val, key in d.items():
    print(key, val)

print(dir(d))

lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
for s in lst:
    print(s[:1])

for idx, s in enumerate(lst):
    print(idx, s)
# _________________________________________________________________________________________________________________________________________________________________________________
#                                                                           Array

from array import *

my_arrays = array('i',[1,2,3,4,5])
print(my_arrays[1])

my_arrays.append(6)
print(my_arrays)

my_arrays.insert(0,0)
print(my_arrays)

my_extends_array = [7,8,9]
my_arrays.extend(my_extends_array)
print(my_arrays)

c = [11,12,13,14]
my_arrays.fromlist(c)
print(my_arrays)

print(my_arrays.index(0))

print(my_arrays.tolist())

d2 = {'key': 'value'}
print(d2)

d2['newkey'] = 42
print(d2)


value = d.setdefault('key', 'default_value')
print(value)

d3 = {'a':1, 'b':2, 'c':3}

for key in d3:
    print(key, d3[key])

for key,value2 in d3.items():
    print(key, value2)

for value3 in d3.values():
    print(value3)

print(d3.items())

my_dict = {'a':[1,2,3], 'b': [1,2,3]}
my_dict['a'].append(4)
print(my_dict)

my_dict['b'].append('four')
print(my_dict)
