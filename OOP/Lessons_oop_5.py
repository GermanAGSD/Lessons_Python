class Vector:
    MAX_COORD = 100
    MIN_COORD = 0

    # Метод класса cls - ссылка на текущий класс
    # можно обращаться к атрибутам класса например MAX_COORD
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x ,y):
        self.x = self.y = 0
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    def get_coords(self):
        return self.x, self.y
    # Статический метод не имеет доступа ни к атрибутам класса
    @staticmethod
    def norm2(x, y):
        return x*x + y*y


v = Vector(1,2)
print(Vector.validate(5))
res = v.get_coords()
print(Vector.norm2(5,6))
print(res)

