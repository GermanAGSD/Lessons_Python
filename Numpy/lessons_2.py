import numpy as np

# Массив из вещественных типов данных
a = np.array([1, 2, 3, 4], 'float64')
print(a)

# Вывести все типы данных у массива Numpy
print(np.sctypeDict)

# Бесзнаковое целое размером 32 бита
b = np.array([1, 2, 3, 4], 'uintc')
print(b)

# Строковое тип данных
c = np.array([1, 2, 3, 4], 'str_')
print(c)

print(np.int16(10.5))

# Двумерный массив
d = np.array([[1,2], [3,4], [5,6]])
print(d)
# Первый срез
print(d[0])
# Второй срез
print(d[1])