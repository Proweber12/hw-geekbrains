class Worker:
    def __init__(self, name, surname, position=None, **kwargs):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = kwargs

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"]+self._income["bonus"]

a = Position("Иван", "Иванов", "Бухгалтер", wage=30000, bonus=5200)
b = Position("Пётр", "Петров", wage=50000, bonus=15000)
print(f'{a.get_full_name()} - {a.get_total_income()}')
print(f'{b.get_full_name()} - {b.get_total_income()}')