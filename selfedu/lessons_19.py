a = 12
b = 7
if a > b:
    res = a
else:
    res = b

s = "python"
t = "upper"

res = s.upper() if t == 'upper' else s
print(res)

a2 = 12
b2 = 7

print([1, 2, a if a > b else b, 4, 5])
