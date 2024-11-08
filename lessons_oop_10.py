from idlelib.debugger_r import close_subprocess_debugger
from string import ascii_letters

from accessify import private, protected

# Property - Свойства
class Person:
    S_RUS = "абвгдежзийклмнопрстуфхцчшщьъэюя-"
    S_RUS_UPPER = S_RUS.upper()
    fio = ''
    old = 0
    ps = ""
    weight = 0

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

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
p = Person("Баклагин Герман Сергеевич", 28, '1234 567890', 90)
