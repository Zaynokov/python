from itertools import count, cycle

start = int(input("С какого числа начать генерацию? - "))
end = int(input("До какого числа генерировать? - "))

for i in count(start):
    if i > end:
        break
    else:
        print(i)

lst = input("Введите элементы списка через пробел: ").split()
cyc = int(input("Сколько кругов сделать? - "))

c = 0
for i in cycle(lst):
    if c == len(lst) * cyc:
        break
    else:
        c += 1
        print(i)
