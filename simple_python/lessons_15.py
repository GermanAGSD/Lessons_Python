a = [1, -54, 3, 23, 43, -45, 0]

a.append(100)
print(a)

a.insert(3, -1000)
print(a)

a.remove(0)
print(a)

print(a.pop())
print(a.pop(3))

c = a.copy()
print(c)
print(id(a))
print(id(c))

print(c.count(1))

print(c.index(1))
print(c.index(1,0))

c.sort()
print(c)

lst = ["Москва", "Казань", "Санкт-Петербург", "Тверь"]
lst.sort()
print(lst)