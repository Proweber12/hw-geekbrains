class Cell:
    def __init__(self, num_cells: int):
        self.num_cells = num_cells

    def __add__(self, other):
        return self.num_cells + other.num_cells

    def __sub__(self, other):
        if (self.num_cells - other.num_cells) > 0:
            return self.num_cells - other.num_cells
        else:
            return "В первой клетке больше ячеек чем во второй, а отрицательный результат не выводится"

    def __mul__(self, other):
        return self.num_cells * other.num_cells

    def __floordiv__(self, other):
        return self.num_cells // other.num_cells

    def make_orders(self, cells_row):
        return '\n'.join(['*' * cells_row for _ in range(self.num_cells // cells_row)]) + '\n' + '*' * (self.num_cells % cells_row)

cell_1 = Cell(54)
cell_2 = Cell(24)

print(cell_2.make_orders(5))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)