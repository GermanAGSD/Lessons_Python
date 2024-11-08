from accessify import private, protected

class Point:

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
        if self.check_value(x) and self.check_value(y):
            # Private __
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coords(self):
        return self.__x, self.__y


pt = Point(1,2)
pt.set_coords(10,20)
print(pt.get_coords())
print("Hello")
