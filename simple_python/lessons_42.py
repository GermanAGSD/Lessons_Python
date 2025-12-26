# Лямбда функции Анонимные
lambda a, b: a + b

a = [4, 5, lambda: print("lambda")]
a[2]()

lst = [5, 3, -6, 8, 10, 1]


def get_filter(a, filter=None):
    if filter is None:
        return a  # Если фильтр не задан, возвращаем весь массив

    res = []
    for x in a:
        if filter(x):
            res.append(x)

    return res  # Возвращаем отфильтрованный результат


r = get_filter(lst, lambda x: x % 2 == 0)
print(r)
