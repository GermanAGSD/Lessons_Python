# Singlton Pattern
import json


class DataBase:
    ipaddress = ""
    user = ""
    passwd = ""
    port = 80

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance is None:
    #         cls.__instance = super().__new__(cls)
    #     return cls.__instance

    def __init__(self, user, passwd, port, ipaddress):
        if not hasattr(self, '_initialized'):  # Чтобы избежать повторной инициализации
            self.ipaddress = ipaddress
            self.user = user
            self.passwd = passwd
            self.port = port
            self._initialized = True

    def __del__(self):
        DataBase.__instance = None

    def update(self, ipaddress, user, passwd, port):
        self.ipaddress = ipaddress
        self.user = user
        self.passwd = passwd
        self.port = port

    def toString(self):
        print(f"Server {self.ipaddress} - {self.user} - {self.passwd} - {self.port}")

    def toJson(self):

        server = {
            "ipaddress": self.ipaddress,
            "User": self.user,
            "passwd": self.passwd,
            "Port": self.port
        }

        json_str = json.dumps(server, indent=4)

        return json_str

    def connect(self):
        print("Соединение")

    def close(self):
        print("Закрытие соединения")

    def read(self):
        print("Чтение данных из бд")
        return "данные из бд"

    def write(self, data):
        print(f"Запись в бд: {data}")

data = DataBase("192.168.1.0","german", "cszc671", 8080)
data.update("192.168.1.2","german", "cszc671", 8080)
data.toString()
print(data.toJson())
print(data)