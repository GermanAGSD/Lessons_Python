# Булевые операции
import numpy as np

a = np.array([1, 2, 3, 10, 20, 30])
# Выделить все что больше 5
f = a[a > 5]
print(f)

b = np.array([1,2,3,4,5,6])
print(a == b)

print(a != b)

c = np.greater(a,b) # Если а больше чем б
print(c)

p = np.less(a,b) # Если а меньше чем б
v = np.equal(a,b) # Если равно

p = np.array([True, False, True, False])
z = np.array([False, True, False, True])

sa = np.logical_and(p,z)
ed = np.logical_or(p,z)
xor = np.logical_xor(p,z)
print(sa)
print(ed)