pass_true = "password"
ps = ""

while ps != pass_true:
    ps = input("vvedite parol: ")
print("Vchod v systemu")

N = 20
i = 1

while i <= N:
    if i % 3 == 0:
        print(i)