import numpy as np
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Вектор и два базиса (как в примере выше)
x = np.array([2, 2], dtype=float)

e1 = np.array([1, 0], dtype=float)
e2 = np.array([0, 1], dtype=float)

b1 = np.array([1, 0], dtype=float)
b2 = np.array([1, 1], dtype=float)

# Координаты x в базисе (b1, b2): x = 0*b1 + 2*b2
alpha, beta = 0, 2
x_from_b = alpha * b1 + beta * b2

fig = plt.figure()
ax = plt.gca()

# Оси
ax.axhline(0)
ax.axvline(0)

def arrow(v, label, text_offset=(0.08, 0.08)):
    ax.arrow(0, 0, v[0], v[1], head_width=0.08, length_includes_head=True)
    ax.text(v[0] + text_offset[0], v[1] + text_offset[1], label)

# Стандартный базис
arrow(e1, "e1")
arrow(e2, "e2")

# Новый базис
arrow(b1, "b1")
arrow(b2, "b2")

# Вектор x
arrow(x, "x = (2,2)", text_offset=(0.10, -0.20))

# Пояснение разложения в новом базисе (на рисунке это тот же вектор)
ax.text(-0.2, 2.6, "x = 2*e1 + 2*e2")
ax.text(-0.2, 2.35, "x = 0*b1 + 2*b2")

ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-0.5, 3.2)
ax.set_ylim(-0.5, 3.0)
ax.set_title("Вектор x в стандартном базисе (e1,e2) и в базисе (b1,b2)")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.tight_layout()
plt.show()
