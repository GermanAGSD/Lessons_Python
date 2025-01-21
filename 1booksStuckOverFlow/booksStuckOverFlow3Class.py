

class D(object):
    multiplier = 12

    @classmethod
    def s(cls, a):
        return cls.multiplier * a

    @staticmethod
    def g(name):
        return (f'Hello {name}')


exz = D()
a = exz.s(2)
s = exz.g('German')
print(a)
print(s)


class Reactangle():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimetr(self):
        return 2 * (self.w + self.h)


class Square(Reactangle):
    def __init__(self, w, h=None):  # h делает необязательным (по умолчанию w = h)
        if h is None:  # Если h не указано, используем w для обеих сторон
            h = w
        super().__init__(w, h)  # Передаём в родительский класс w и h


# Поскольку у квадрата равные стороны то передается s

# class Square(Reactangle):
#     def __init__(self,s):
#         super().__init__(s,s)
#         self.s = s

squ = Square(2, 2)

print(squ.perimetr())
print(issubclass(Square, Reactangle))
print(isinstance(squ, Square))


class Person(object):

    def __init__(self, first_name, last_name, age):
        if last_name is None:
            self.first_name, self.last_name = first_name.split("", 2)
        else:
            self.first_name = first_name
            self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name
        self.age = age

    def greet(self):
        print(f"Здраствуйте меня зовут {self.full_name}")


p = Person('German', 'Baklagin', 29)
p.greet()


class Country:
    def __init__(self, cities=None):
        self.cities = cities if cities else []

    def addCity(self, city):
        self.cities.append(city)


class City:
    def __init__(self, numPeople):
        self.people = []
        self.numPeople = numPeople
        self.country = None  # Добавляем ссылку на страну

    def addPerson(self, person):
        self.people.append(person)

    def join_country(self, country):
        self.country = country  # Связываем город со страной
        country.addCity(self)
        for i in range(self.numPeople):
            person = Person(i)
            person.join_city(self)


class Person:
    def __init__(self, ID):
        self.ID = ID
        self.city = None  # Ссылка на город

    def join_city(self, city):
        self.city = city  # Связываем человека с городом
        city.addPerson(self)

    def people_in_my_country(self):
        # Считаем всех людей во всех городах страны
        return sum(len(city.people) for city in self.city.country.cities)


# Создаём страну
US = Country()

# Создаём города и связываем их с страной
NYC = City(10)
NYC.join_country(US)

SF = City(5)
SF.join_country(US)

# Вывод количества людей в стране из первого человека в Нью-Йорке
print(US.cities[0].people[0].people_in_my_country())
