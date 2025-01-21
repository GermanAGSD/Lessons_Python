# Примеры с операторами цикла for Факториал
def factorial():
    n = int(input("Введите натуральное число"))
    if n < 1 or n > 100:
        print("Неврное введено натуральное число")
    else:
        p = 1
        for i in range(1, n + 1):
            p *= i
        print(f"Факториал {n}! = {p}")




def eleochka():
    for i in range(1, 7):
        print('*' * i)




def words():
    words = ["Python", "day", "mne", "sily"]
    S = ''
    for i in words:
        S += ' ' + i
    print(S.lstrip())

words()


def words2():
    words = ["Python", "day", "mne", "sily"]
    print(" ".join(words))

words2()


def lessons_23():
    digs = [4, 3, 100, -53, -30, 1, 34, -8, 10]
    for i in range(len(digs)):
        if 10 <= abs(digs[i]) <= 99:
            digs[i] = 0
    print(digs)


lessons_23()

# Перевод в латиницу