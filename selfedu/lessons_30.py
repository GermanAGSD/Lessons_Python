# Словари перебор элементов словаря в цикле
lst = ["+7", "+6", "+5", "+4"]
a = dict.fromkeys(lst)
print(a)
a = dict.fromkeys(lst, "код страны")
d2 = a.copy()
print(a)
a.clear()
print(a)
print(d2)
d22 = d2.get("+7")
print(d22)


