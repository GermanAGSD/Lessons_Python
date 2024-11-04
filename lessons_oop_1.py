class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Вызов init")

    def __del__(self):
        print("Удаление" + str(self))

    def set_coords(self, x , y):
        self.x = x
        self.y = y
        print("Вызов set coords" + str(self))

    def get_coords(self):
        return (self.x, self.y)

pt = Point(1,2)
pt.set_coords(1,2)
print(pt.get_coords())