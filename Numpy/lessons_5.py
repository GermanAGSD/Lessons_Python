# Изменение формы массивов добавление и удаление осей
import numpy as np

a = np.arange(10)
print(a)
a.shape = 2, 5
print(a)
b = a.reshape(10)
print(b)

# Создание одного вектора из матрицы
azr = np.full((3,3),3)
print(azr.ravel())

azq = np.array([[1,2,3], [3,4,5], [5,6,7]])
azq.resize(3,3,refcheck=False)
print(azq)
# Ресайз если не совпадает размерость то будет заполненость 0
azq.resize(4,5,refcheck=False)
print(azq)

x_test = np.arange(32).reshape(8,2,2)
print(x_test)
# Добавить новую ось
x_test2 = np.expand_dims(x_test, axis=0)
print(x_test2.shape)
print(x_test2)