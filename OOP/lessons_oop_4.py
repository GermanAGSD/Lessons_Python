from calendar import prcal


class Point:

    # cls ссылка на текущий экзепляр класса Point
    def __new__(cls, *args, **kwargs):
        print("Вызов new для" + str(cls))
        # Адрес нового созданного объекта
        return super().__new__(cls)

    # self ссылается на создаваемый экзепляр класса
    def __init__(self, x = 0, y=0):
        print("Вызов init")
        self.x = x
        self.y = y

pt = Point(1,2)
print(pt)