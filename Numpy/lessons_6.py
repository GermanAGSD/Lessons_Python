# Объеденение и разделение масивов
import numpy as np
from torch import dtype

a = np.array([(1,2), (3,4)])
b = np.array([(5,6), (7,8)])

# Объеденение по горизонтали
c = np.hstack([a,b])
print(c)

# Объеденение по вертикали
d = np.vstack([a,b])
print(d)

e = np.fromiter(range(18), dtype='int32')
i = np.fromiter(range(18,36), dtype='int32')

e.resize(3,3,2)
g = i.resize(3,3,2)
print(e)