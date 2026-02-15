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