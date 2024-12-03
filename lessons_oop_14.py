# Магический метод
# __add__ для операций  сложения
# __sub__ для операций вычитания
# __mul__ для операций умножения
# __truediv__ для операций деления

class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)} : {self.__get_formatted(m)} : {self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть целым числом")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд или int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds += sc
        return self
    def __imul__(self, other):
        print("__imul__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд или int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds += sc
        return self

c1 = Clock(1000)
c2 = Clock(1000)
c1 += 100
c1 *= 2
c3 = c1 + c2
# c1 = c1 + 100
print(c3.get_time())
print(c1.get_time())