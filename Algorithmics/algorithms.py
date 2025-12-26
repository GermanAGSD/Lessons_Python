 # метод наименьших квадратов
 # f (x) = kx + b
#  Для отклонений можно взять сумму квадратов ошибок отклонений
#  Сумма всех i = 1; N; (y[i] - f(x[i]))^2
import numpy as np
import matplotlib.pyplot as plt

# число эксперементов
N = 100
# стандартное отклонение наблюдаемых значений
sigma = 3
# теоретическое значеие парраметра k
k = 0.5
# теоретическое значеие парраметра k
b = 2

f = np.array([k*z+b for z in range(N)])
y = f + np.random.normal(0, sigma, N)

x = np.array(range(N))

mx = x.sum() / N
my = y.sum() / N
a2 = np.dot(x.T, x) / N
a11 = np.dot(x.T, y) / N

kk = (a11 - mx*my)/(a2 - mx**2)
bb = my - kk*mx

ff = np.array([kk*z+b for z in range(N)])
plt.plot(f)
plt.plot(ff, c='red')
plt.scatter(x, y, s=2, c='red')
plt.grid(True)
plt.show()