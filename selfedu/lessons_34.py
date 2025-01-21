# set Генераторы множества

a = {x ** 2 for x in range(1, 5)}
print(a)
# Генерация словаря
b = {x: x ** 2 for x in range(1, 5)}
print(b)
# Генерация множества
d = [1, 2, '1', '2', -4, 3, 4, True]
set_d = set()
for x in d:
    set_d.add(int(x))
print(set_d)



