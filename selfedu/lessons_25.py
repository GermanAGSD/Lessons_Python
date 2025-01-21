# Вложенные циклы
from asyncio import eager_task_factory


def lessons_25():
    for i in range(1, 4):
        for j in range(1, 6):
            print(f"i = {i} j = {j}", end='')
        print()


lessons_25()


def lessons_25_2():
    a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    for row in a:
        print(row, type(row))
        for x in row:
            print(x, type(x), end=' ')


# lessons_25_2()


def lessons_25_3():
    a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
    c = []
    # Получить индекс и значение
    for i, row in enumerate(a):
        r = []
        for j, x in enumerate(row):
            r.append(x + b[i][j])
        c.append(r)
    print(c)


lessons_25_3()


def lessons_25_4():
    ds = [1, 2, 3, 4]
    for i, k in enumerate(ds):
        print(i, k)


lessons_25_4()


def lessons_25_5():
    M, N = list(map(int, input("Zadej M N: ").split()))
    zeros = []
    for i in range(M):
        zeros.append([0] * N)
    print(zeros)

    for i in range(M):
        for j in range(N):
            zeros[i][j] = 1
    print(zeros)

lessons_25_5()
