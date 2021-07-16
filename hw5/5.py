class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки {self.title}"


class Pen(Stationery):
    def draw(self):
        return f"Запуск отрисовки {self.title}"


class Pencil(Stationery):
    def draw(self):
        return f"Запуск отрисовки {self.title}"


class Handle(Stationery):
    def draw(self):
        return f"Запуск отрисовки {self.title}"

stationery = Stationery("чем-то")
pen = Pen("ручкой")
pencil = Pencil("карандашом")
handle = Handle("маркером")

print(stationery.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
