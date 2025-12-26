# Итерируемый объект
d = [5,3,7,10,32]

it = iter(d)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

s = "python"
it2 = iter(s)
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

for x in "python":
    print(x)

