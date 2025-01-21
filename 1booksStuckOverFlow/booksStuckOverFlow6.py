import collections
import json
from fileinput import filename

from mypy.util import json_dumps

counts = collections.Counter([1,2,3])
print(counts)

# Json Открытие файла и запись в формате Json
d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1,2,3]
}

json_str = json.dumps(d)

with open('../selfedu/out.json', 'w') as f:
    json.dump(json_str,f)

# Json Чтение из файла
with open('../selfedu/out.json', 'r') as f:
    d = json.load(f)
print(d)

# Сортировка ключей по алф порядку
d2 = {
    'id': 1,
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1,2,3]
}

print(json.dumps(d2, sort_keys=True))
json_s = json.dumps(d2)

# Создание словаря из Json
dictJson = json.loads(json_s)
print(dictJson)