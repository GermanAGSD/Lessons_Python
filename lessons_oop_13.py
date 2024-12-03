# Магический метол __str__ __repr__ __len__ __abs__
# __str__ Для отображения информации об объекте класса для пользователей например для функции print, str
# __repr__ Для отображения информации об объекте класса в режиме отладки
class Cat:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__} : {self.name}"

    def __str__(self):
        return f"{self.name}"

    def __len__(self):
        return

cat = Cat("Муся")
print(cat)

class Point:

    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    # Сформируем список который будет состоять из модулей координат, применим abs ко каждуому элементу коллекции coords
    def __abs__(self):
        return list(map(abs, self.__coords))

p = Point(1,-2, -5)
print(len(p))
print(abs(p))