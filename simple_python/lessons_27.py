# Генераторы списков
N = 6
a = [0] * N
for i in range(N):
    a[i] = i ** 2
print(a)

b = [x ** 2 for x in range(N)]
print(b)

d_inp = input("Целые числа через пробел: ")
a = [int(d) for d in d_inp.split()]
print(d_inp.split())

squares = [x * x for x in range(5)]
print(squares)

squares2 = []
for x in (0,1,2,3,4):
    squares2.append(x*x)
print(sorted(squares2))
