# Перезаписать файл (удалит старое содержимое)
import mmap
import os.path

with open('somefile.txt', 'w', encoding='utf-8') as fileobj:
    fileobj.write("tomato\npasta\nnglarg\n")

with open('somefile.txt', 'r', encoding='utf-8') as fileobj:
    lines = fileobj.readlines()
    print(lines)

with open('somefile.txt', 'r', encoding='utf-8') as fileobj:
    lines = [line.strip() for line in fileobj]   # убирает \n и пробелы по краям
    print(lines)

with open('somefile.txt', 'r+b') as fd:
    mm = mmap.mmap(fd.fileno(),0, access=mmap.ACCESS_READ)
    print(mm[5:10])

p = os.path.join(os.getcwd(), 'somefile.txt')
print(p)

pr = os.path.exists(p)
print(pr)