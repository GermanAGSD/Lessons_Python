# Магический метод
# getitem, setitem delitem
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный index")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен ьыть целым")
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

s1 = Student("Germna", [2,3,5,5,6])
s1[9] = 1
print(s1[9])
print(s1.marks)