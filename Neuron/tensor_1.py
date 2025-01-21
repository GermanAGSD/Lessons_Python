from array import array
from functools import total_ordering

import torch
import numpy as np
t = torch.Tensor(3,5,2)
t2 = torch.empty(3,5,2, dtype=torch.int32)
# Matrice размерностью
t3 = torch.tensor([1,2,0])
d = [[1,2,3], [4,5,6]]
t4 = torch.tensor(d, dtype=torch.float32)
print(t)
print(t2)
print(t3)
print(t4)
# type
print(t.type())
# количество осей
print(t4.dim())
# количество элементов на каждой оси
print(t4.size())

d_np = np.array([[1,2,3], [4,5,6]])
t5 = torch.from_numpy(d_np)
print(t5)
t6 = torch.tensor(d_np, dtype=torch.float32)
print(t6)
d = t4.numpy()
d = t4.numpy().copy()
print(torch.cuda.is_available())