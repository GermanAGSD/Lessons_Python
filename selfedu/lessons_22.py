# Оператор цикла for
def cykle():
    d = [1,2,3,4,5]
    p = 1
    for n in d:
        p*=n
    print(p)
cykle()
def cykle2():
    d = [1,2,3,4,5]
    for i in range(len(d)):
        d[i] = 0
    print(d)
cykle2()

def cykle3():
    a = list(range(0,5))
    print(a)
cykle3()

def cykle4():
    S = 0
    for i in range(2, 1001):
        S += 1/i
    print(S)
cykle4()