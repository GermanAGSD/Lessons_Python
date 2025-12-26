# FileNot Found Error
try:
    file = open("myFile.txt", encoding='utf-8')
    try:
        s = file.readlines()
        print(s)
        file.close()
    finally:
        file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлами")


# FileNot Found Error
try:
    with open("myFile.txt", encoding='utf-8') as file:
        s = file.readlines()
        print(s)
    # try:
    #     s = file.readlines()
    #     print(s)
    #     file.close()
    # finally:
    #     file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлами")

