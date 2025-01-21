# random
import random
from random import gauss

a = random.random()
b = random.uniform(1,5)
c = random.randint(-3,7)
d = random.randrange(-3,7, 2)
print(a)
print(b)
print(c)
print(d)

# Гаусовские случайные величина
g = random.gauss(0, 3.5)
print(g)
lst = [4,5,6,7,8,9,1]
h = random.choice(lst)
z = random.shuffle(lst)
print(h)
print(z)