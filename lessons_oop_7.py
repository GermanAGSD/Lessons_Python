from idlelib.debugger_r import close_subprocess_debugger
# Магические методы __setattr и тд
from accessify import private, protected

class Point:
    MAX_COORD = 100
    MIN_COORD = 0
    def __init__(self, x = 0, y = 0):
        # Protected _
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self._x = x
            self._y = y
            
    @private
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

    def set_coords(self, x, y):
        if self.check_value(x) and self.check_value(y) and self.MIN_COORD <= x <= self.MAX_COORD :
            # Private __
            self.__x = x
            self.__y = y

        else:
            raise ValueError("Координаты должны быть числами")

    # Если функция принимает self то значение класса не меняется, только локальное свойство
    # Если функция принимает cls то переменная класса будет изменена на то значение которым иницилизируется
    @classmethod
    def set_bound_Min_or_Max(cls, max, min):
        cls.MIN_COORD = min
        cls.MAX_COORD = max

    # Не будет изменяться
    def set_bound2(self, left):
        self.MIN_COORD = left

    @classmethod
    def validata(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def get_coords(self):
        return self.__x, self.__y

    # Автоматически вызывается при получении свойства класса с именем item
    # item атрибут к которому идет обращение
    def __getattribute__(self, item):
        print("__getattribute__")
        # Запретить обращаться к аттрибуту x
        if item == "_x":
            raise ValueError("Доступ запрещен")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print("__setattr__")

        if key == "z":
            raise AttributeError("недопустимое имя аттрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print("__getattr__" + item)
        return False

    def __delattr__(self, item):
        print("__delattr__" + item)
        object.__delattr__(self, item)

pt = Point(1,2)
pt.set_coords(10,20)
pt.set_bound_Min_or_Max(101, -100)
print(pt.y)
print(pt.validata(102))
print(pt.__dict__)
print(Point.__dict__)
del pt._x