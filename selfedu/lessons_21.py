from lib2to3.fixes.fix_input import context

print("start")

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
