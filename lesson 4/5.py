from functools import reduce
lst = [i for i in range(100, 1001, 2)]


def func(pre, fut):
    return pre * fut


print(reduce(func, lst))
