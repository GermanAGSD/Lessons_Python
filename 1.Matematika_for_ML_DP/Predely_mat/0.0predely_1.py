import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.pyplot as plt

# ______________________________________________________________________________________
# Аналитическая геометрия

# Вычисление пределов
x = sp.symbols('x')
expr = sp.sin(x)/x
res = sp.limit(expr,x,0)
print(res)
# ______________________________________________________________________________________
# Пределы на бесконечности
expr1 = (1 + 1/x)**x
result = sp.limit(expr1, x, sp.oo)
print(result)  # E

# ______________________________________________________________________________________
# Объявляем символьную переменную
n2 = sp.Symbol('n', integer=True, positive=True)
# Исходное выражение
expr2 = (5*n2 + 6) / (n2 + 1)
# Вычисляем предел при n -> ∞ (5n+6)/(n+1)
limit_value = sp.limit(expr2, n2, sp.oo)
print(f"Предел выражения (5n+6)/(n+1) при n→∞: {limit_value}")  # 5

# ______________________________________________________________________________________
# Вычисляем предел при n -> ∞ sin(n)/(n)
n3 = sp.Symbol('n', integer=True, positive=True)
expr3 = sp.sin(n3)/n3
limit = sp.limit(expr3, n3, sp.oo)
print(f"Предел выражения sin(n)/(n) при n→∞: {limit}")  # 5
# ______________________________________________________________________________________

# Решение логарифмов
# 1 способ
ab = np.log(100000)/np.log(3)
# 2 способ
ac = math.log(100000)/math.log(3)
print(ac)
print(ab)