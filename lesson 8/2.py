class DivisionZero(Exception):
    def __init__(self, txt):
        self.txt = txt


divisible = input("Введиет делимое: ")
divisor = input("Введите делитель: ")
try:
    if divisible.isdigit() and int(divisor) == 0:
        raise DivisionZero("На ноль делить нельзя")
    else:
        print(int(divisible) / int(divisor))
except ValueError:
    print("Вы ввели не число")
except DivisionZero as error:
    print(error)

print("Программа завершила свою работу")
