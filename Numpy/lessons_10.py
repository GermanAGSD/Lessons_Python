# Базовые мат операции
import numpy as np

a = np.array([1,2,3,10,20,30])
s = a.sum()
d = a.min()
print(s)
a.resize(3,2)
print(a)

print(a.sum(axis=0))

# Модуль
print(np.abs(a))
print(np.amax(a))
print(np.amin(a))

r = np.linspace(0, np.pi, 10)
print(r)
ert = np.sin(r)
print(ert)

yt = np.random.rand(3,3)
print(yt)

np.random.seed(13)
rt = np.random.randint(10,size=10)
print(rt)