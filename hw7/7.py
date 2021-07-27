class ComplexNumbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        num1 = self.num1 + other.num1
        num2 = self.num2 + other.num2
        return ComplexNumbers(num1, num2)

    def __mul__(self, other):
        num1 = self.num1 * other.num1
        num2 = self.num2 * other.num2
        return ComplexNumbers(num1, num2)

    def __str__(self):
        return f'{self.num1} + {self.num2}i'

a = ComplexNumbers(1, 2)
b = ComplexNumbers(2, 3)

print(a)
print(b)
print(a + b)
print(a * b)