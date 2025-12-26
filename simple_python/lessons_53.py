import pickle, os
# Запись данных
# w в текстовом на запись
try:
    with open("out.json", "a", encoding='utf-8') as file:
        file.write("Hello\n")
        file.write("Hello2\n")
        file.write("Hello3\n")
except:
    print("Error")

# И добавлять и считывать
# w в текстовом на запись
try:
    with open("out.json", "a+ ", encoding='utf-8') as file:
        file.write("Hello\n")
        file.write("Hello2\n")
        file.write("Hello3\n")
    # raise FileNotFoundError
except:
    print("Error")

books = [
    ("Евгений Онегин", "Пушкин А С", 200)
]

# Запись в бинарном режиме
file = open("out.bin", "wb")
pickle.dump(books, file)
file.close()

# Чтение бинарного файла
file = open("out.bin", "rb")
ps = pickle.load(file)
file.close()
print(ps)

# Получить текущюю директорию
p = os.path.join(os.getcwd())
print(p)