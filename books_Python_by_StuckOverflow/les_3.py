# __________________________________________________________________________________________________________________________________________________________________________________
#                                                                           Списки
from selfedu.lessons_70 import title

a = [1, 2, 3, 4, 5]
a.append(6)
a.append(7)
a.append(8)
print(a)

b = [8, 9]
a.append(b)
print(a)

my_string = "hello world"
a.append(my_string)
print(a)

a2 = [1, 2, 3, 4, 5, 6, 7, 7]
b2 = [8, 9]

a2.append(b)
print([8])

a2.extend(b2)
print(a2)

c = a2.index(3)
print(c)

a2.insert(0, 0)
print(a2)

# Delete
print(a2.pop(2))

a2.remove(0)

c2 = a2.reverse()
print(a2)

# Кол-во вхождений
print(a2.count(7))


a2.reverse()

a3 = [1, 2, 3, 4, 5, 6, 7, 7]
a3.insert(4, 10)
a3.sort()
print(a3)

lst = []
if not lst:
    print("Empty List")

my_list = ['foo', 'bar', 'baz']

for item in my_list:
    print(item)

for (index, items) in enumerate(my_list):
    print("The item in position {} is {}".format(index, items))

for i in range(0, len(my_list)):
    print(my_list[i])

print('foo' in my_list)

# Все ли значения True
nums = [1, 1, 0, 1]
print(all(nums))
print(any(nums))

a_list = ['a1', 'a2', 'a3']
b_list = ['b1', 'b2', 'b3']

for (a, b) in zip(a_list, b_list):
    print(a, b)

squares = [x * x for x in (1, 2, 3, 4)]
print(squares)

gen = [x for x in range(10) if x % 2 == 0]
print(gen)

# str 153 BOOKS_________________________________________________________________________________________________________________________________________________________________
#                                                              Кортежи
import heapq

numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
nlarge = heapq.nlargest(4, numbers)
print(nlarge)

print(heapq.heapify(numbers))

t = tuple('lupins')
print(t)

t2 = (1,4,9)
# t2[0] = 2
print(t2)

t3 = (1,2)
q=t3
t3 += (3,4)
print(t3)

# Кортеж
a = (1,)


x,y,z = (1,2,3,)
print(x,y,z)

list = [1,2,3,4,5]
print(tuple(list))

