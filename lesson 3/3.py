def my_func(arg1, arg2, arg3):
    return arg1 + arg2 + arg3 - min(arg1, arg2, arg3)


while True:
    arg1 = input("Введите первый аргумент: ")
    helper = arg1.replace(".", "")
    helper = helper.replace("-", "")
    if helper.isdigit():
        arg1 = float(arg1)
        break
while True:
    arg2 = input("Введите первый аргумент: ")
    helper = arg2.replace(".", "")
    helper = helper.replace("-", "")
    if helper.isdigit():
        arg2 = float(arg2)
        break
while True:
    arg3 = input("Введите первый аргумент: ")
    helper = arg3.replace(".", "")
    helper = helper.replace("-", "")
    if helper.isdigit():
        arg3 = float(arg3)
        break

print(my_func(arg1, arg2, arg3))
