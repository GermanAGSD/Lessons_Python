# Функции
import math

def lessons_36():
    text = "Письмо"
    print(text)
    return text


lessons_36()


def get_sqrt(x):
    res = None if x < 0 else math.sqrt(x)
    return res, x


def get_max_2(a,b):
    return a if a > b else b

a, b = get_sqrt(49)
print(a, b)

x, y = 5, 7
print(get_max_2(x,y))

