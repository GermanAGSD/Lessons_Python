# Наследование


class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self):
        print("Painting geom")

class Line(Geom):
    name = 'Line'
    def draw(self):
        print("Painting line")

class Rect(Geom):
    name = 'Rect'
    def draw(self):
        print("Painting Rect")


l = Line()
r = Rect()
l.set_coords(x1=1,x2=1,y1=2,y2=2)
r.set_coords(1,1,2,2)
print(l.name)
print(r.name)