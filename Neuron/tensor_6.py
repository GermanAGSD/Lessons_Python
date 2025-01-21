from array import array
from functools import total_ordering

import torch
import numpy as np
# Математические операции
a = torch.FloatTensor([1,2,3])
# Вычитание
print(a - 3)
# Унарный оператор
print(-a)
print(a + 2)

b = torch.IntTensor([3,4,5])
print(a - b)

a2 = torch.arange(1,19).view(3,3,2)
b2 = torch.ones(3,2)

print(a2 - b2)
print(a2 * b2)
print(a2 // b2)

a3 = torch.arange(4)
a4 = torch.arange(4)
print(a3.add(a4))
# Изменяет тензор а3
print(a3.add_(a4))