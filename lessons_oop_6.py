class Point:

    def __init__(self, x = 0, y = 0):
        # Protected _
        self._x = x
        self._y = y

    def set_coords(self, x, y):
        # Private __
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


pt = Point(1,2)
pt.set_coords(10,20)
print(pt.get_coords())
print("Hello")
