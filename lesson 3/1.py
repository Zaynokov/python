while True:
    dividend = input("Введите делимое: ")
    helper = dividend.replace(".", "")
    helper = helper.replace("-", "")
    if helper.isdigit():
        dividend = float(dividend)
        break
while True:
    divider = input("Введите делитель: ")
    helper = divider.replace(".", "")
    helper = helper.replace("-", "")
    if helper.isdigit():
        divider = float(divider)
        break


def div_func(a, b):
    return a / b if b != 0 else "На ноль делить нельзя!"


print(div_func(dividend, divider))
