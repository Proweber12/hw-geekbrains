from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size_or_height, name=None):
        self.size_or_height = size_or_height
        self.name = name

    @abstractmethod
    def consum(self):
        pass

    def __add__(self, other):
        return self.consum + other.consum


class Coat(Clothes):
    @property
    def consum(self):
        return round(self.size_or_height / 6.5, 1) + 0.5


class Suit(Clothes):
    @property
    def consum(self):
        return 2 * self.size_or_height + 0.3


c = Coat(48)
s = Suit(190)
print(c.consum)
print(s.consum)
print(c + s)
