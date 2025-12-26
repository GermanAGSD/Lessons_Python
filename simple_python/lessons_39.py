# Функция с произвольным числом парраметров args kwargs
m = max(1,2,3,4,-5)
print(m)

def os_path(*args, sep='\\',**kwargs):
    path = sep.join(args)
    print(args)
    print(kwargs)
    return path

p = os_path('F:\\~stepil', "dobry python", sep='/', trim=True)
print(p)