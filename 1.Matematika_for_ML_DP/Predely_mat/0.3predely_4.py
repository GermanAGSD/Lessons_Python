import sympy as sp
import matplotlib.pyplot as plt
import math
import numpy as np

# ___________________________________________________________________________________
# Предел функции
x = sp.Symbol('x')
expr = sp.sin(x) / x
limit_val = sp.limit(expr, x, 0)
print(f"Предел при x→0: {limit_val}")  # Вывод: 1

# ___________________________________________________________________________________
# Предел функции
expr = (1 + 1/x)**x
limit_val = sp.limit(expr, x, sp.oo)
print(f"Предел при x→∞: {limit_val}")  # Вывод: E (число e)
# ___________________________________________________________________________________
# Предел функции
expr = (x**2 - 1) / (x - 1)
limit_val = sp.limit(expr, x, 1)
print(f"Предел при x→1: {limit_val}")  # 2