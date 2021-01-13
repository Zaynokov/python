usr_lst = input("Введите элементы списка через пробел: ")
usr_lst = "".join(i for i in usr_lst if i.isdigit() or i == " ").split()
usr_lst = [int(i) for i in usr_lst]

print(f"Введенный список: {usr_lst}")
print(f"Результат: {[i for i in usr_lst if usr_lst.count(i) == 1]}")
