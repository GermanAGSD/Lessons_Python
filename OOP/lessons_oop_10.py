import json
from idlelib.debugger_r import close_subprocess_debugger
from string import ascii_letters

from accessify import private, protected

# Property - Свойства
from string import ascii_letters
import hashlib
from array_lessons import json_string


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight, password):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_passport(ps)
        self.verify_weight(weight)
        self.hash_password(password)
        self.__fio = self.capitalize_each_word(fio).split()  # Применяем метод для заглавных букв
        self.__old = old
        self.__passport = ps
        self.__weight = weight
        self.__password = self.hash_password(password)

    def toString(self):
        # Форматируем вывод в консоль
        print(f"ФИО: {' '.join(self.__fio)}, Возраст: {self.__old}, Паспорт: {self.__passport}, Вес: {self.__weight}")

    def to_dict(self):
        return {
            "fio": ' '.join(self.__fio),
            "old": self.__old,
            "passport": self.__passport,
            "weigth": self.__weight,
            "password": self.__password
        }

    def toJson(self):
        json_str = self.to_dict()
        return json.dumps(json_str, ensure_ascii=False, indent=4)

    @private
    @classmethod
    def hash_password(cls, password: str) -> str:
        sha256 = hashlib.sha256()
        sha256.update(password.encode("utf-8"))
        return sha256.hexdigest()


    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("Fio not String")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Formatted FIO = 3 object")

        letter = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("Must be > 1 symbols")
            if len(s.strip(letter)) != 0:
                raise TypeError("Must use rus symbol and -")

    @classmethod
    def capitalize_each_word(cls, fio):
        return fio.title()  # Применяем метод title для приведения первых букв к заглавным

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть в пределах 14 - 120")

    @classmethod
    def verify_weight(cls, w):
        if type(w) != int or w < 20:
            raise TypeError("Возраст должен быть в пределах 14 - 120")

    @classmethod
    def verify_passport(cls, ps: str):

        if type(ps) != str:
            raise TypeError("Пасспорт должен быть строкой")
        s = ps.split()

        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) !=6:
            raise TypeError("Пасспорт серия номер ")
        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер должны быть числами")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport

# Пример использования
person = Person("иванов иван иванович", 30, "1234 567890", 20, "password")
print(person.toJson())
person.toString()

