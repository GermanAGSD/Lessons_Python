import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.pyplot as plt

def draw_grid(ax, A=None, lim=3, n_lines=13, n_points=200, label_prefix=""):
    ts = np.linspace(-lim, lim, n_lines)
    ys = np.linspace(-lim, lim, n_points)
    xs = np.linspace(-lim, lim, n_points)

    # Вертикальные линии x = t
    for t in ts:
        pts = np.vstack([np.full_like(ys, t), ys])  # (2, n_points)
        if A is not None:
            pts = A @ pts
        ax.plot(pts[0], pts[1], alpha=0.6)

    # Горизонтальные линии y = t
    for t in ts:
        pts = np.vstack([xs, np.full_like(xs, t)])
        if A is not None:
            pts = A @ pts
        ax.plot(pts[0], pts[1], alpha=0.6)

def plot_transform(A, title):
    fig = plt.figure()
    ax = plt.gca()

    # Оси
    ax.axhline(0)
    ax.axvline(0)

    # Исходная сетка (I)
    draw_grid(ax, A=None, lim=3, n_lines=13, n_points=200)

    # Преобразованная сетка
    draw_grid(ax, A=A, lim=3, n_lines=13, n_points=200)

    # Базисные векторы и их образы
    e1 = np.array([[1.0], [0.0]])
    e2 = np.array([[0.0], [1.0]])
    Ae1 = A @ e1
    Ae2 = A @ e2

    ax.arrow(0, 0, e1[0,0], e1[1,0], head_width=0.12, length_includes_head=True)
    ax.arrow(0, 0, e2[0,0], e2[1,0], head_width=0.12, length_includes_head=True)
    ax.text(1.05, 0.05, "e1")
    ax.text(0.05, 1.05, "e2")

    ax.arrow(0, 0, Ae1[0,0], Ae1[1,0], head_width=0.12, length_includes_head=True)
    ax.arrow(0, 0, Ae2[0,0], Ae2[1,0], head_width=0.12, length_includes_head=True)
    ax.text(Ae1[0,0]*1.05, Ae1[1,0]*1.05, "A e1")
    ax.text(Ae2[0,0]*1.05, Ae2[1,0]*1.05, "A e2")

    ax.set_aspect('equal', adjustable='box')
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.tight_layout()
    plt.show()

# --- Матрицы из примера ---
A1 = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
               [np.sin(np.pi/4),  np.cos(np.pi/4)]], dtype=float)

A2 = np.array([[2, 0],
               [0, 1]], dtype=float)

A3 = 0.5 * np.array([[3, -1],
                     [1, -1]], dtype=float)

plot_transform(A1, "A1: поворот на 45° (π/4)")
plot_transform(A2, "A2: растяжение по x в 2 раза")
plot_transform(A3, "A3: общее линейное преобразование")
