# set Множества
a = {1,2,3, "hello", 2,3}
print(a, type(a))
aa = {1,2,3, "hello", 2,3, (True, 4)}
print(aa, type(aa))
print(type(set()))
cities = ['Kaluga', 'Krasnodar', 'Tumen','Ulynovsk']
a2 = set(cities)
for c in a2:
    print(c)

a2.add(7)
print(a2)
a2.update(["a", "b"])
print(a2)
a2.discard('a')
print(a2)
