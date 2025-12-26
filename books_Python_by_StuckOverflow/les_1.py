print({1, 2, 3, 4, 5, 6}.intersection({3, 4, 5, 6}))
print({1, 2, 3, 4, 5, 6}.union({3, 4, 5, 6}))
print({1, 2, 3, 4}.difference({2, 3, 5}))
print({1, 2, 3, 4}.symmetric_difference({2, 3, 5}))

print(2 in {1, 2, 3})
print(4 not in {1, 2, 3})

s = {1, 2, 3}
s.add(4)
print(s)

s.discard(4)
print(s)

s.remove(2)
print(s)

a = {1, 2, 2, 3, 4}
b = {3, 3, 4, 4, 5}

d = a.intersection(b)
print("Intersection: ", d)

setA = {'a', 'b', 'b', 'c'}
print(setA)

listA = ['a', 'b', 'b', 'c']
print(listA)

a, b, c, d = 2, 3, 5, 7
print(b)

dd = a**(b+c)
print(dd)