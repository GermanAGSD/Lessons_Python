# Индексация срезы итерирование массивов
import numpy as np


a = np.arange(12)
a[-1] # Последний элемент массива

b = a[2:4]
print(b)

x = np.array([(1,2,4), (10,20,30), (100,200,300)])
print(x)
print(x[1,1])
print(x[1,:])