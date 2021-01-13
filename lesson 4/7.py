n = int(input("Факториал какого числа нужно получить? - "))


def func(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f


for el in func(n):
    print(el)
