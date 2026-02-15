import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.pyplot as plt

# ______________________________________________________________________________________
# Аналитическая геометрия


# Евклидова норма L2 - обычная длина пример x = (3,4)
x = np.array([3,4])
NX = np.linalg.norm(x)
print(NX)

# Манхэттенская норма пример x = (3,-4,2)
A = np.array([3,-4,2])
NM = np.linalg.norm(A, ord=1)
print(NM)

# Норма L максимальная пример x = (3,-4,2)

B = np.array([3,-4,2])
MB = np.linalg.norm(B, ord=np.inf)
print(MB)

# Расстояние между двумя точками
a1 = np.array([1,2])
b1 = np.array([4,6])
dist = np.linalg.norm(a1-b1)   # L2 расстояние
print(dist)

# Норма матрицы
AZ = np.array([[1,2],[3,4]])
AZN = np.linalg.norm(AZ, 'fro')
print(AZN)