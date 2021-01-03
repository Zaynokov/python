while True:
    x = input("Введите действительное положительное число x: ")
    helper = x.replace(".", "")
    if helper.isdigit() and int(helper) > 0:
        x = float(x)
        break
while True:
    y = input("Введите целое отрицательное число y: ")
    helper = helper.replace("-", "")
    if helper.isdigit() and "-" in y and not "." in y:
        y = int(y)
        break


def my_func(x, y):
    for i in range(-y - 1):
        x *= x
    return 1 / x


print(my_func(x, y))
