# Чтение данных из файла
# только чтение
file = open("myFile.txt", encoding='utf-8')

# print(file.read())
# file.seek(0)

# # Прочитать 4 символа
# print(file.read(4))

# pos = file.tell()
# print(pos)

# Прочитать первую строку
print(file.readline())

# Прочитать построчно файл
for line in file:
    print(line)
file.seek(0)
# Прочитать весь файл
print(file.readlines())
file.close()