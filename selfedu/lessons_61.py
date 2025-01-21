# is instnce

a = 5
print(isinstance(a, int))
data = (4.5, 8.7, True, "book", 8, 10, -11)

s = sum(filter(lambda x: isinstance(x, float), data))
s2 = sum(filter(lambda x: type(x) is int, data))
print(s)
print(s2)

# s = 0
# for x in data:
#     if isinstance(x, float):
#         s +=x
#
# print(s)
