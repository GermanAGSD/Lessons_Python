import math
from datetime import datetime, timedelta
from enum import Enum
from array import *
# Переменные
a = 2
b = 923322232323
pi = 3.14159
q = True
k = 1j
str = 'Hello German'
print(type(str))
print(type(k))
print(type(q))
print(type(a))
print(type(pi))

# Списки
c = [1,2,3,4,5,6,7,8,9]
# Вложенные списки
c = [1,2,[3,4,5],6,7,8,9]
# Отступы блоков
def my_function():
    d = 2
    return d
res = my_function()
print(res)
# Последовательности и коллекции
# В python различают упорядоченные последовательности и неупорядоченные
# такие как set dict
r = reversed("Germa n")
print(r)
# Преобразование между типами данных
a = '123'
b = int(a)
c = '123.456'
b = float(c)
print(type(c))
print(type(b))

# Добавление в список
names = ['German', 'Alex']
names.append("Alex")
# Index
names.insert(4, 'Vova')
names.remove("Vova")
print(len(names))
print(names)
# Подсчет количества вхождение любого элемента в списке
a =[1,2,3,4,5,6]
print(a.count(1))
# Обратить последовательность
a.reverse()
print(a)
# Перебор элементов
for element in a:
    print(element)
# Кортежи
ip_address = ("10.20.10.20", 8080)
# Словарь
state_capital = {
    "Arkansas":'Little Rock',
    "Colorado": "Denver"
}
print(state_capital)
ca_capital = state_capital['Colorado']
print(ca_capital)
for l in state_capital.keys():
    print(l)
# Set набор
my_list = [1,2,3]
my_set = set(my_list)

# Ввод данных
# name = input("")

print(dir(math))
sqr = math.sqrt(4)
now = datetime.now()
then = datetime(2024,5,23)
delta = now - then
print(delta)

# Перечисления Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3
print(Color.green)

# Итерация
class Color2(Enum):
    red_1 = 1
    red_2 = 2
    red_3 = 3

[c for c in Color]

# Glava 8
# Пересечения
var_peresecenie = {1,2,3,4,5}.intersection({3,4,5})
print(var_peresecenie)
# Объеденение
var_obedenenie = {1,2,3,4,5}.union({3,4,5,6})
print(var_obedenenie)
# Разница
var_raznica = {1,2,3,4}.difference({2,3,5})
print(var_raznica)
# Симметричная разность
var_symetric = {1,2,3,4}.symmetric_difference({2,3,4})
print(var_symetric)
# Проверка суперпозици
var_superpozici = {1,2,3}.issuperset({1,2,3})
print(var_superpozici)
# Добавление и удаление из множества
s = {1,2,3}
s.add(4)
s.discard(3)
s.remove(2)

# Получение уникальных значений
restaraunt = ['MCDonalds', 'Burger King','MCDonalds','Chiken']
unique_rest = set(restaraunt)
# Преобразование обратно в список
var_list = list(unique_rest)
print(unique_rest)
i = 0
list_n = [1,2,3,4,5]
# Способ 1x632
# Способ 2
for k in list_n:
    i+=1
    res += k
    pass
print(res)
print("Qty number: ", i)

global m,n,v
# Вывод локальных и Глобальных переменных
print("Local: ", locals().keys())
print("Global: ", globals().keys())

def descriminant(a, b, c):
    decr = (b * b) - 4 *(a * c)
    return decr
result = descriminant(2,4,2)
print(result)

# Множества Set frozenset
a = set('abracadabra') # Дубликаты будут удалены
print(a)
a.add('z')
print(a)
b = frozenset('asdfagsa')
print(b)

