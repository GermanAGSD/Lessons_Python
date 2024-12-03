# a.dtype - тип массива
# a = np.array([1,2,3,4,5,6,7,8,9]) чтобы преобразовать в матрицу 3*3 b = a.reshape(3,3)
# np.sctypeDict - типы данных
import numpy as np

nulmatice = np.array([0] * 10)
print(nulmatice)
empt = np.empty(10)
print(empt)
ones = np.eye(4)
print(ones)
ones2 = np.eye(4,2)
print(ones2)
ident = np.identity(5)
print(ident)
ones3 = np.ones([4,3])
print(ones3)
ful = np.full((3,2), -1)
print(ful)
diag = np.diag([1,2,3])
print(diag)