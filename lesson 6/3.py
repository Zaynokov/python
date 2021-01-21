class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 25000, "bonus": 4500}


class Position(Worker):

    def get_full_name(self):
        return f"Полное имя: {self.name} {self.surname}"

    def get_total_income(self):
        return f"Доход: {self._income['wage'] + self._income['bonus']}"


man = Position("Сергей", "Смирнов", "Мастер")
print(man.get_full_name())
print((man.get_total_income()))
