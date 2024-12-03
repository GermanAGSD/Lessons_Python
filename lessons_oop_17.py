# Магический метод
# bool len


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print("__bool__")
        return  self.x  == self.y


pt = Point(1,1)
print(bool(pt))
if pt:
    print("Object True")
else:
    print("Object False")