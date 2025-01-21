# Десриптор данных get set
class Integer:

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Кордината должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f"f __set__: {self.name} = {value}")
        setattr(instance, self.name, value)


class Point3D:
    # Дескриптор данных
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Кордината должна быть целым числом")

    # @property
    # def x(self):
    #     return self._x
    #
    # @x.setter
    # def x(self, coord):
    #     self.verify_coord(coord)
    #     self._x = coord
    #
    # @property
    # def y(self):
    #     return self._y
    #
    # @y.setter
    # def y(self, coord):
    #     self.verify_coord(coord)
    #     self._y = coord
    #
    # @property
    # def z(self):
    #     return self._z
    #
    # @z.setter
    # def z(self, coord):
    #     self.verify_coord(coord)
    #     self._z = coord

p = Point3D(1,2,3)
print(p.__dict__)