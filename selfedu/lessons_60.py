# sort
def is_odd(x):
    return x % 2


a = [4, 3, -10, 1, 7, 12]
b = sorted(a, key=is_odd)
b2 = sorted(a, key=lambda x: x % 2)
print(b)
print(b2)


def ket_sort(x):
    return x if x % 2 == 0 else 100 + x
