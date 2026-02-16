import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

# Значения n (натуральные числа)
n_values = np.arange(1, 101)  # от 1 до 100
x_n = (1 + 1/n_values) ** n_values

# Число e для сравнения
e = np.exp(1)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(n_values, x_n, 'b-', linewidth=2, label=r'$X_n = (1+1/n)^n$')
plt.axhline(y=e, color='r', linestyle='--', linewidth=2, label=r'$e \approx 2.71828$')

# Настройка осей
plt.xlabel('n', fontsize=14)
plt.ylabel('X_n', fontsize=14)
plt.title('Сходимость последовательности к числу e', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.xlim(1, 100)
plt.ylim(2.5, 2.75)

# Показать график
plt.show()