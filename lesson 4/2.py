usr_lst = input("Введите элементы списка через пробел: ")
usr_lst = "".join(i for i in usr_lst if i.isdigit() or i == " ").split()

print(f"Введенный список: {usr_lst}")
print(f"Результат: {[int(usr_lst[i]) for i in range(1, len(usr_lst)) if int(usr_lst[i]) > int(usr_lst[i - 1])]}")
