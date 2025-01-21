# Is subclass Наследование от встроенных типов


class Geom:
    name = "Geom"
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y2 = y2
        self.x2 = x2
        self.y1 = y1
        print(f"Init {self.__class__}")

class Line(Geom):

    def draw(self):
        print("Painting line")

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(self,x1, y1, x2, y2)
        self.fill = fill
        print("Init line")

    def draw(self):
        print("Painting Rect")

l = Line(0,0,10 ,20)

r = Rect(1,2,3,5)
print(l.__dict__)