def my_func(x, y):
    return x ** y


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
print(my_func(x, y))
