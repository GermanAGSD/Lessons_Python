var = [1, 2, 3, 4]

it = iter(var)
print(next(it))
print(next(it))

s = "Строка"
s_iter = iter(s)
print(next(s_iter))
print(s_iter.__next__())
print(s_iter.__reduce__())

print(range(5))

n = 50_000_000

print(list(range(1, 5)))
print(list(s))

x = list(range(n))
# print(x)

z = []
for i in x:
    z.append(i ** 2)
print(sum(z))

y = map(lambda val: val ** 2, x)


def gen(n):
    for i in range(n):
        yield i ** 2

print(sum(gen(n)))

g = gen(10)

for i in g:
    print(i)

for i in range(5):
    if i == 2:
        break
    print(i)