# Is subclass Наследование от встроенных типов


class Geom:
    pass

class Line(Geom):
    pass

# Переопределние класса List
class Vector(list):
    def __str__(self):
        return  " ".join(map(str, self))



g = Geom()
l = Line()
print(issubclass(Line, Geom))
print(Geom.__name__)

v = Vector([1,2,3])
print(v)