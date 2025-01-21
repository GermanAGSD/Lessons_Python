# filter
a = [1,2,3,4]
b = filter(lambda x: x % 2 ==0, a)

# lst = list(b)

for x in b:
    print(x)

def is_prost(x):
    d = x -1
    if d <0:
        return False
    while d > 1:
        if x % d == 0:
            return False
        d -= 1

    return True

c = filter(is_prost, a)
lst = list(c)
print(lst)

lst2 = ("Москва", "Рязань1", "Смоленск")
b2 = filter(str.isalpha, lst2)
print(list(b2))
