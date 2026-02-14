import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# --- 1) Синтетические данные в 3D, которые почти лежат в 2D-подпространстве ---
np.random.seed(42)

n = 500

# 2 скрытых фактора (истинное "низкоразмерное" пространство)
z_true = np.random.randn(n, 2)

# Линейное отображение из 2D -> 3D (столбцы задают базис подпространства)
W_true = np.array([[2.0, 0.5],
                   [0.3, 1.5],
                   [-1.2, 0.7]])  # shape (3,2)

# Сдвиг (среднее) — чтобы было похоже на реальные данные
mu = np.array([10.0, -5.0, 3.0])

# Данные: X = mu + Z*W^T + шум
noise = 0.15 * np.random.randn(n, 3)
X = mu + z_true @ W_true.T + noise  # shape (n,3)

# --- 2) PCA через SVD ---
X_centered = X - X.mean(axis=0)  # центрируем (важно!)
U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

# Главные направления (строки Vt), берём первые 2 — это базис 2D-подпространства в 3D
components = Vt[:2, :]  # shape (2,3)

# Доля объяснённой дисперсии
explained_var = (S**2) / (n - 1)
explained_ratio = explained_var / explained_var.sum()

print("Главные компоненты (2 направления в 3D) [строки — PC1 и PC2]:")
print(components)
print("\nДоли объяснённой дисперсии:")
print("PC1:", float(explained_ratio[0]))
print("PC2:", float(explained_ratio[1]))
print("PC3:", float(explained_ratio[2]))
print("Суммарно PC1+PC2:", float(explained_ratio[0] + explained_ratio[1]))

# --- 3) Проекция на найденное 2D-подпространство и восстановление обратно в 3D ---
Z = X_centered @ components.T           # координаты в 2D (n,2)
X_hat = Z @ components + X.mean(axis=0) # восстановление в 3D (n,3)

rmse = np.sqrt(np.mean((X - X_hat) ** 2))
print("\nRMSE восстановления (среднеквадр. ошибка):", float(rmse))

# --- 4) Графики ---

# 4.1) 3D: исходные точки + восстановленные
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], s=10, alpha=0.5, label="Исходные точки")
ax.scatter(X_hat[:, 0], X_hat[:, 1], X_hat[:, 2], s=10, alpha=0.5, label="Проекция на 2D (PCA)")
ax.set_title("3D данные и их проекция на 2D-подпространство (PCA)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()
plt.tight_layout()
plt.show()

# 4.2) 2D: точки в координатах главных компонент (снижение размерности)
fig = plt.figure()
plt.scatter(Z[:, 0], Z[:, 1], s=10, alpha=0.7)
plt.title("Данные в 2D после PCA (координаты PC1 и PC2)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.tight_layout()
plt.show()
