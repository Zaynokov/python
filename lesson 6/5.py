class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки маркером")


Pen("Ручка").draw()
Pencil("Карандаш").draw()
Handle("Маркер").draw()
