# Именованные аргумента Фактические и формальные парраметры
def get_v(a, b, c, verbose=True):
    if verbose:
        return a * b * c


v = get_v(1, 2, 3, True)
print(v)


def cmp_str(s1, s2, reg=False, trim=True):
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:
        s1 = s1.strip()
        s2 = s2.strip()
    return s1 == s2

print(cmp_str("Python", "Python", trim=False))

def add_value(value, lst=None):
    if lst == None:
        lst = []
    lst.append(value)
    return lst

l = add_value(1)
l = add_value(2)

print(l)