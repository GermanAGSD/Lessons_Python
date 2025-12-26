class Counter:
    def __init__(self):
        self.__counter

    def __cal__(self, *args, **kwargs):
        self.__counter + 1
        print("__cal__")
        return self.__counter

c = Counter()
c2 = Counter()
c()
c()