import numpy as np
import sympy as sp

# Нахождение базиса
# ______________________________________________________________________________________
v1 = sp.Matrix([1,2,3])
v2 = sp.Matrix([2,4,6])
v3 = sp.Matrix([1,0,1])

A = sp.Matrix.hstack(v1, v2, v3)   # столбцы
rrefA, pivots = A.rref()
basis = [A.col(i) for i in pivots]
print("pivot columns:", pivots)
print("basis:", basis)

#
# ______________________________________________________________________________________
# Найти ранг
B = np.array([[1,2,3],
              [2,4,6],
              [1,0,1]], dtype=float)

r = np.linalg.matrix_rank(B)
print(f"Ранг ",r)  # 2
# ______________________________________________________________________________________
# Найти ранг
C = np.array([[3,2,1,0,4],[2,1,-3,1,2],[6,7,3,2,2]])
CR = np.linalg.matrix_rank(C)
print(f'Ранг матрицы С ', CR)
