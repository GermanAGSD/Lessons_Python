import os
# Создание директории
try:
    os.makedirs("./dir1/subdir1")
except FileExistsError:
    print('Директория существует')


# Создание директории
try:
    os.mkdir("newDir", mode=777)
except FileExistsError:
    print('Директория существует')

print(os.name)