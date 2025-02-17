# Произведение матриц и векторов элементы линейной алгебры
from operator import matmul

import numpy as np

# Произведение матриц а и б
a = np.array([(1, 2, 3), (4, 1, 4), (3, 6, 7)])
b = np.array([(3, 2, 1), (1, 1, 2), (2, 3, 7)])
res = np.dot(a, b)
print(res)

# 2 Вариант умножения матриц
res2 = matmul(a, b)
print(res2)

g = np.array([1, 2, 3])
rt = np.arange(4, 10).reshape(3, 2)

print(f" * {np.dot(g, rt)}")

# Вычеслить ранг матрицы
ry = np.array([(1, 2, 3), (1, 4, 9), (1, 8, 27)])
er = np.linalg.matrix_rank(a)
print(er)

# Решение уровнения ry
y = np.array([10, 20, 30])
po = np.linalg.solve(ry,y)
print(po)

# 2 вариант решения с обратной матрицей
uy = np.linalg.inv(ry)
per = np.matmul(ry,uy)
print(per)

# Корни уравнения
ert = np.dot(uy,y)
print(ert)

# Детерминант матрицы
determ = np.linalg.det(ry)
print(determ)