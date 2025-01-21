from accessify import private, protected
from typing import Any, Optional

class Point:
    """
       set and get coordinate
    """

    def __init__(self, x = 0, y = 0):
        # Private
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            # Private
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def check_value(cls, value):
        return type(value) in (int, float)

    def set_coords(self, x, y) -> None:
        if self.check_value(x) and self.check_value(y):
            # Private __
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coords(self) -> list[Any]:
        return [self.__x, self.__y]


pt = Point(1,2)
pt.set_coords(10,20)
print(pt.get_coords())
print("Hello")
print(dir(pt))
