from array import array
from functools import total_ordering
from traceback import print_tb

import torch
import numpy as np
# Тригонометрические и статические функции
a = torch.FloatTensor([1,2,3,10,20,30])
print(a)

# Вычеслить сумму всех элементов тензора
print(a.sum().item)
# Среднее значение элементов
print(a.mean())
# Максимальное значение элементов
print(a.max())
# Преобразование тензора в 3 х 2
print(a.view(3,2))
# Сумма по определенным осям
print(a.sum(dim=0))
# Работа с многомерными тензорами
print(a.amax(dim=0))
print(a.amin(dim=0))

a2 = torch.IntTensor([-1,1,5,-44,32,2])
# Модули этих значений
print(torch.abs(a2))
print(torch.amax(a2))
print(torch.log(a2))
print(torch.round(a2))
print(a2.float())
print(a2.log())

print(a.round())

a = torch.linspace(0, torch.pi, 10)
print(a)
r = torch.sin(a)
print(r)
y = torch.FloatTensor([1,4,3,7,10,8,14,21,20,23])
x = torch.FloatTensor([4,1,6,9,12,11,16,19,15,22])
m = torch.median(x)
print(m)
d = x.var()
print(d)
xy = torch.vstack([x,y])
res = torch.corrcoef(xy)
print(res)