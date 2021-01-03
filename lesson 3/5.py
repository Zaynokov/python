summa = 0
while input("Нажмите Enter для начала. Для выхода введите q ").lower() != "q":
    num_lst = input("Введите строку чисел, разделенных пробелом: ").split()
    for i in num_lst:
        if i.isdigit():
            summa += int(i)
        else:
            input("Вы ввели не число. Можете продолжить, нажав Enter")
    print(summa)
