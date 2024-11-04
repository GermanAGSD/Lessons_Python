
from array import *
import json
# Массивы
my_array = array('i',[1,2,3,4,5])
print(my_array[0])
#
my_array.append(6)
my_array.insert(0,5)
print("Получение значения по индексу",my_array.index(1))
# Количество вхождений в массив

print("Количество вхождений: ",my_array.count(1))
for i in my_array:
    print(i)

#
# Многомерные массивы
lst = [[1,2,3],[4,5,6],[7,8,9]]
# Обращение к элементам
print(lst[0])
print(lst[0][0])

# Словарь d = {"key": "value"}
data = "value"
slovar = {
    "key": "value",
    "key2": "value2"
}
print(slovar['key'])
json_string = json.dumps(slovar)
print(json_string)
print(slovar.keys())
print(slovar.values())
print(slovar.items())

stock = {
    "eggs": 5,
    "milk": 2
}

dictionry = {}
dictionry["eggs"] = 5
dictionry["milk"] = 2
print(dictionry)

mydict = {'a':[1,2,3], 'b':[1,2,3]}
mydict["a"].append(4)
print(mydict)
json_dict = json.dumps(mydict, indent=3)
print("Json String", json_dict)
# Создание упорядоченного словаря
from collections import OrderedDict
d = OrderedDict()
d["first"] = 1
d["second"] = 2
for key in d:
    print(key, d[key])
