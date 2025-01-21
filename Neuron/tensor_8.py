from array import array
from functools import total_ordering
from traceback import print_tb

import torch
import numpy as np
# Векторно матричное действие

a = torch.arange(1,10).view(3, 3)
b = torch.arange(10,19).view(3, 3)
print(a)
print(b)

r1 = a*b
print(r1)
r2 = torch.mul(a,b)
print(r2)
c = torch.matmul(a,b)
print(c)
v = torch.LongTensor([-1,-2,-3])
c = torch.matmul(a,v)
print(c)
# 7 матрицы 3 х 5
bx = torch.randn(7,3,5)
by = torch.randn(7,5,4)
bc = torch.bmm(bx, by)
print(bc)
print(bc.size())
# Вектора умножить
aa = torch.arange(1,10, dtype=torch.int32)
ab = torch.ones(9, dtype=torch.int32)
print(aa)
print(ab)
# Скалярное произведение
cc = torch.dot(aa,ab)
print(cc)
# Внешнее произведение
sa = torch.outer(aa,ab)
print(sa)
# Умножение вектора на матрицу

af = torch.arange(1,10, dtype=torch.int32).view(3,3)
ag = torch.arange(1,4, dtype=torch.int32)
print(af)
print(ag)
res2 = torch.mv(af, ag)
print(res2)
# Решение линейных уравнений
aq = torch.FloatTensor([(1,2,3), (1,4,9), (1,8,27)])
print(aq)
# Вычислить ранг
res3 = torch.linalg.matrix_rank(aq)
print(res3)
yy = torch.FloatTensor([10,20,30])
# Корни линейного уравнения
res4 = torch.linalg.solve(aq, yy)
print(res4)

# 2 способ решения
# Вычисление обратной матрицы
inva = torch.linalg.inv(aq)
# Записать векторно матричное произведение
xc = torch.mv(inva, yy)
print(xc)