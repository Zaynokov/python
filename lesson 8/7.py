class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        result = ''
        real = self.re + other.re
        imaginary = self.im + other.im
        if real == 0 and imaginary < 0:
            result += f"-j{abs(imaginary)}"
        elif real == 0 and imaginary > 0:
            result += f"j{imaginary}"
        elif real != 0:
            result += f"{real} {'+ j' if imaginary > 0 else '- j'}{abs(imaginary)}"
        else:
            result = '0'
        return 'Сумма равна: ' + result

    def __mul__(self, other):
        result = ''
        real = self.re * other.re + (- self.im * other.im)
        imaginary = self.re * other.im + self.im * other.re
        if real == 0 and imaginary < 0:
            result += f"-j{abs(imaginary)}"
        elif real == 0 and imaginary > 0:
            result += f"j{imaginary}"
        elif real != 0:
            result += f"{real} {'+ j' if imaginary > 0 else '- j'}{abs(imaginary)}"
        else:
            result = '0'
        return 'Произведение равно: ' + result

    def __str__(self):
        result = ''
        if self.re == 0 and self.im < 0:
            result += f"-j{abs(self.im)}"
        elif self.re == 0 and self.im > 0:
            result += f"j{self.im}"
        elif self.re != 0:
            result += f"{self.re} {'+ j' if self.im > 0 else '- j'}{abs(self.im)}"
        else:
            result = '0'
        return result


a = ComplexNum(0, 0)
b = ComplexNum(6, 3)
print(a)
print(b)
print(a + b)
print(a * b)
