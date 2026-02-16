import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.pyplot as plt

# ______________________________________________________________________________
# Найти факториал
f = math.factorial(5)
print(f'Факториал ',f)

# Найти факториал
n = sp.Symbol('n', integer=True, positive=True)
expr = (sp.factorial(n+1) + sp.factorial(n+3)) / sp.factorial(n+2)
limit = sp.limit(expr, n, sp.oo)
print(limit)  # (бесконечность)