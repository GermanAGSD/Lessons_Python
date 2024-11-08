from idlelib.debugger_r import close_subprocess_debugger
from accessify import private, protected

# Паттерн моносостояния
class ThreadData:

    __shared_attrs__ = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    # Когда будет создаваться экземпляр класса то коллекция dict,будет ссылаться на словарь __shared_attrs__\
    # Локальные свойства будут едиными для всех экзепляров класса
    # th = ThreadData()
    # th2 = ThreadData()
    # th.id = 1 Это свойство будет у всех экземпяров класса
    def __init__(self):
        self.__dict__ = self.__shared_attrs__

    def print(self):
        return self.__shared_attrs__

th = ThreadData()
th2 = ThreadData()
th.id = 1
print(th.print())
print(th2.print())