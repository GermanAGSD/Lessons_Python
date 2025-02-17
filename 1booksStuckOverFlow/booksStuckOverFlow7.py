import sqlite3

def sqlite3Mod(databaseName, queryGet = None, queryPost = None):

    try:

        # Подключение к базе данных
        conn = sqlite3.connect(databaseName)
        c = conn.cursor()
        # Создать таблицу, если она не существует
        c.execute("CREATE TABLE test (date TEXT)")
        print("Таблица успешно создана.")
    except sqlite3.OperationalError as e:
        # Проверить, если ошибка вызвана существованием таблицы
        if "table test already exists" in str(e):
            print("Таблица уже существует, продолжаем выполнение.")
            if queryPost != None:
                c.execute(queryPost)
                conn.commit()
            if queryGet != None:
                c.execute(queryGet)
            return c.fetchall()
        else:
            # Пробросить исключение для других ошибок
            raise
    finally:
        # Закрытие соединения
        conn.close()

row = sqlite3Mod(databaseName='example.db',queryGet="SELECT * FROM test")
a = list(row)
print(a)
