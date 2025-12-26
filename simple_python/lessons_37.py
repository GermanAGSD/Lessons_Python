# Функции Алгоритм Евклида

def get_node(a, b):
    """
    Вычисляется node для натуральных чисел по алгоритму
    Евклида
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


res = get_node(18,24)
print(res)
help(get_node)

def test_nod(func):
    # --- test ---
    a = 28
    b = 35
    res = func(a,b)
    if res == 7:
        print("test 1 ok")
    else:
        print("test fail")

test_nod(get_node)