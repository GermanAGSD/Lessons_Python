import torch
import matplotlib.pyplot as plt

N = 5
b = 3
# Генерация данных для класса C1
x1 = torch.rand(N)
x2 = x1 + torch.randint(1, 10, [N]) / 10 + b
C1 = torch.vstack([x1, x2, torch.ones(N)]).mT

# Генерация данных для класса C2
x1 = torch.randn(N)
x2 = x1 - torch.randint(1, 10, [N]) / 10 + b
C2 = torch.vstack([x1, x2, torch.ones(N)]).mT

# Линия разделения и веса
f = [0 + b, 1 + b]
w1 = -0.5
w2 = -w1
w3 = -b * w2
w = torch.FloatTensor([w1, w2, w3])  # Вектор из 2 элементов

# Проверка каждого элемента
for i in range(N):
    x = C1[i]
    y = torch.dot(w, x)
    if y >= 0:
        print(f"Точка {x} принадлежит классу C1")
    else:
        print(f"Точка {x} принадлежит классу C2")

# Визуализация
plt.scatter(C1[:, 0], C1[:, 1], s=10, c='red', label='C1')
plt.scatter(C2[:, 0], C2[:, 1], s=10, c='blue', label='C2')
plt.plot(f)
plt.grid()
plt.legend()
plt.show()
