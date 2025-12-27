#
# x = -4
# if x < 0:
#     x = -x
# print(x)
#
# marks = [4,4,3,5,2]
# if 2 in marks:
#     print("Студент будет отчислен")
# else:
#     print("Студент сдал сессию")
#
# print("start")

def lessons_21():
    d = [1,2,3,5,6,0,-4]
    i = 0
    flFind = False
    while i < len(d) and d[i] % 2 != 0:
        print(i)
        flFind = d[i] % 2 == 0
        if flFind:
            break

        i += 1
    print(flFind)

lessons_21()