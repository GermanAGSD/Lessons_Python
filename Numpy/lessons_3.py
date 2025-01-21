# Функции автозаполнения создание матриц и числовых диапазонов
import numpy as np

nulmatice = np.array([0] * 10)
print(nulmatice)
onematice = np.array([1] * 9)
print(onematice)
a = onematice.reshape(3,3)
print(a)
# Любой массив любой размерности
b = np.empty(10)
c = np.empty((3,2), dtype='int16')
print(c)
# Еденицы по главной диагонале 4 мерный массив
d = np.eye(4)
print(d)

# Массив из 1 по главной диогонале
c = np.identity(5)
print(c)
# Массив из нулей
e = np.zeros((3,3))
print(e)
# Массив из едениц
f = np.ones((3,3))
print(f)

# Произволбные массивы из заданных чисел
g = np.full((3,4), -1)
print(g)

# Создает матрицу 1х4 из строки
h = np.asmatrix('1 2 3 4')
ad = np.asmatrix('1 2; 3 4')
print(h)
print(ad)

# Диагональная матрицы
aq = np.diag([1,2,3])
print(aq)
# Выделяет элементы по главной диагонали
aw = np.diag([(1,2,3), (4,5,6), (7,8,9)])
print(aw)

df = np.arange(5)
print(df)

dg = np.linspace(0, np.pi, 3)
print(dg)

sdf = np.linspace(0,1,3)
print(sdf)

def getRange(x,y):
    return 100 * x * y

aq = np.fromfunction(getRange, (2,2))
print(f"aq={aq}")

def getRange2(N):
    for i in range(N):
        yield i

az = np.fromiter(getRange2(4), 'int8')
print(az)

ag = np.fromstring('1 2 3', 'int16', sep=' ')
agd = np.fromstring('1, 2, 3', 'int16', sep=',')
print(ag)
print(agd)