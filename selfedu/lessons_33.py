# set Операции над Множества
setA = {1,2,3,4}
setB = {3,4,5,6,7}
# Пересение множества
res  = setA & setB
print(res)

# Пересение множества
res2 = setA.intersection(setB)
print(res2)

# Объеденение множества
setT = {1,2,3,4}
setC = {3,4,5,6,7}

res3 = setT | setC
print(res3)

res4 = setT.union(setC)
print(res4)
# Вычитание одного из другого
setX = {1,2,3,4}
setY = {3,4,5,6,7}

res5 = setX - setY
print(res5)
# Симметрична разность
setZ = {1,2,3,4}
setV = {3,4,5,6,7}

res6 = setZ ^ setV
print(res6)

# Сравнение между собой
setU = {7,6,5,4,3}
setI = {3,4,5,6,7}
res7 = setU == setI
print(res7)