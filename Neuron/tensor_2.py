from array import array
from functools import total_ordering

import torch
import numpy as np

from SSE.SSEserver import print_active_hosts

# Матрица из нулей
tz = torch.zeros(2,3, dtype=torch.int32)
print(tz)
# Матрица из едениц
t1 = torch.ones(2,3)
print(t1)
# Формирование единичной матрицы по диагонали
t2 = torch.eye(3,3)
print(t2)
# Формирование матрицы определенного размера и заполненостью определенными значениями
t3 = torch.full((3,3), 5)
print(t3)
# Диапазоны чисел ар  прогрессией с шагом
t4 = torch.arange(-5, 0, 2)
print(t4)
# Формирование чисел определенного диапазона
t5 = torch.linspace(1,5,1)
print(t5)
# Тензор со случайными значениями от нуля до
t6 = torch.rand(3,3)
t7 = torch.randn(3,3)
print(t6)
print(t7)
# Виды методом inplace _ с подчеркиванием изменяет текущей тензор не создавая нового
# Формирует новый тензор
t8 = torch.IntTensor(2,5).zero_()
# Заменить все числа другими например еденицами
t8.fill_(1)
print(t8)
# Заполнить тензор гаусовскими значениями
t6.normal_(0,1)
print(t8)
# Создать тензор из вещественных чисел и заполнить нулями
t9 = torch.FloatTensor(2,5).zero_()
print(t9)
# Заполнить определенными значениями
t10 = torch.FloatTensor(2,5).fill_(10)
print(t10)
# Представление 3 Х 9
t11 = torch.arange(27)
t11.view(3,9)
t11[0] = 100
print(t11)
# Изменить размерность тензора
t11.reshape(3,3,3)
print(t11)
t12 = torch.full((3,3), 5)
t13 = torch.full((3,3), 5)
t14 = torch.full((3,3), 5)
t12.resize_(2,3)
print(t12)
# Вытянуть вектор
t13.ravel()
print(t13)
# Изменить оси местами
# t13.permute()
print(t13)
# Транспонирование
print(t14.mT)
