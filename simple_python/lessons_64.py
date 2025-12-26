# Расширенное представление чисел
flags = 5
mask = 4
res = flags & mask
print(res)

bit_0 = 8
bit_1 = 5
bit_0 = bit_0 | bit_1
print(bit_0)

bit_2 = 9
bit_3 = 1
bit_2 = bit_2 ^ bit_3
print(bit_2)
print(bin(bit_2))

# Смещение вправо влево
x = 160
x = x >> 1

ac = 0b0010001
print("0b011", ac)
print(x)
print(bin(x))