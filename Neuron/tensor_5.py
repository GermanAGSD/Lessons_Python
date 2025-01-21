from array import array
from functools import total_ordering

import torch
import numpy as np
# Индексация и срезы
a = torch.arange(12)
print(a[2])
print(a[2].item())
print(a[-1])
a[0] = 100
print(a[0].item())
b = a[2:4]
print(b)
print(a[:5])
print(a[-1:5])
print(a[:])
print(a[1:6:2])
# Индексирование
a2 = torch.arange(8)
print(a2[0])
print(a2[0].item)
