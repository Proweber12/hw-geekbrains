class Matrix:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return '\n'.join(map(str, self.args))

    def __add__(self, other):
        list_sum = []
        for lists_vol in range(len(self.args)):
            list_sum.append([])
            for el in range(len(self.args[0])):
                list_sum[lists_vol].append(self.args[lists_vol][el] + other.args[lists_vol][el])
        return '\n'.join(map(str, list_sum))


a = Matrix([0, 1, 2], [4, 5, 6])
b = Matrix([6, 5, 4], [2, 1, 0])

print(a, '\n')
print(b, '\n')
print(a + b)