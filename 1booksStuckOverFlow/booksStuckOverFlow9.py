# Комбинации
import itertools

a = [1,2,3,4,5,6]
b = list(itertools.combinations(a,2))
print(len(b))
print(b)