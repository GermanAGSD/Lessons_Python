import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

A = np.array([[2,1,3,-5],[-1,3,2,-4],[3,2,-1,1],[1,1,3,-2]])

b = np.array([-4,-8,14,-4])
det = np.linalg.det(A)
print(det)

z = np.linalg.inv(A) @ b
print(z)

# Пересечение плоскостей является точка [3,1,-2,1]
# Решение (лучше solve, чем inv)
x = np.linalg.solve(A, b)
x1_0, x2_0, x3_0, x4_0 = x
print("x =", x)

# --- 3D-срез: фиксируем x4 = найденному значению ---
R = 5
N = 60
xs = np.linspace(x1_0 - R, x1_0 + R, N)
ys = np.linspace(x2_0 - R, x2_0 + R, N)
X1, X2 = np.meshgrid(xs, ys)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Каждое уравнение: a1*x1 + a2*x2 + a3*x3 + a4*x4 = bi
# При фиксированном x4 = x4_0 выражаем x3:
# x3 = (bi - a1*x1 - a2*x2 - a4*x4_0) / a3
for i in range(4):
    a1, a2, a3, a4 = A[i]
    bi = b[i]
    Z = (bi - a1*X1 - a2*X2 - a4*x4_0) / a3
    ax.plot_surface(X1, X2, Z, alpha=0.30)

# Точка пересечения (в этом срезе)
ax.scatter([x1_0], [x2_0], [x3_0], s=80)
ax.text(x1_0, x2_0, x3_0, f"  ({x1_0:.0f}, {x2_0:.0f}, {x3_0:.0f}), x4={x4_0:.0f}")

ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("x3")
ax.set_title("Срез в R^4: плоскости при фиксированном x4 (график в x1-x2-x3)")

plt.tight_layout()
plt.show()
