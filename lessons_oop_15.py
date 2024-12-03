# Магический метод
# eq, lt

class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod
    def verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен быть int or Clock")
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.verify_data(other)
        return self.seconds > sc

s1 = Clock(1000)
s2 = Clock(1000)
print(s1 < s2)
print(s1 > s2)
print(s1 != s2)
print(s1 == s2)
