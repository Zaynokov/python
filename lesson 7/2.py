from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, V, H):
        self.V = V
        self.H = H

    def cloth(self):
        return f"Всего ткани необходимо: {self.V / 6.5 + 0.5 + 2 * self.H + 0.3:.2f}"

    @abstractmethod
    def description(self):
        return "Одежда"


class Coat(Clothes):

    @property
    def cloth(self):
        return f"Ткани для производства пальто необходимо: {self.V / 6.5 + 0.5:.2f}"

    def description(self):
        return "Пальто"


class Suit(Clothes):
    def cloth(self):
        return f"Ткани для производства костюма необходимо: {2 * self.H + 0.3:.2f}"

    def description(self):
        return "Костюм"


coat = Coat(350, 51)
suit = Suit(350, 51)
print(coat.cloth)
print(suit.cloth())
print(coat.description())
print(suit.description())
