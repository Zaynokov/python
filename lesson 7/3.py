class Cell:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other):
        return self.cell_count + other.cell_count

    def __sub__(self, other):
        sub = self.cell_count - other.cell_count
        return sub if sub > 0 else "Разность количества ячеек двух клеток меньше нуля"

    def __mul__(self, other):
        return self.cell_count * other.cell_count

    def __truediv__(self, other):
        return self.cell_count // other.cell_count

    def make_order(self, count_in_row):
        result = ""
        for i in range(self.cell_count // count_in_row):
            result += "*" * count_in_row + "\n"
        result += "*" * (self.cell_count % count_in_row)
        return result


first_cell = Cell(30)
second_cell = Cell(18)
print(first_cell + second_cell)
print(first_cell - second_cell)
print(first_cell * second_cell)
print(first_cell / second_cell)
print(first_cell.make_order(8))
