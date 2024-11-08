from idlelib.debugger_r import close_subprocess_debugger
from accessify import private, protected

# Property - Свойства
class Person:
    name = ''
    old = 0

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def get_old(self):
        return self.__old

    @get_old.setter
    def set_old(self, old):
        self.__old = old



p = Person("German", 28)
p2 = Person("German", 29)
# p.get_old(35)
#
print(p.get_old, p.__dict__)