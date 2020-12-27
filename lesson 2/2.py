n = input("Введите количество элементов списка (целое положительное число) - ")

start_list = []
change_list = []

while True:
    if n.isdigit():
        for i in range(int(n)):
            start_list.append(input(f"Введите {i + 1}-й элемент списка - "))
        for i in range(len(start_list)):
            if i == int(n) - 1 and int(n) % 2 != 0:
                change_list.append(start_list[i])
                break
            elif i % 2 == 0:
                change_list.append(start_list[i+1])
            else:
                change_list.append(start_list[i-1])
        break
    else:
        n = input("Пожалуйста, введите целое положительное число - ")

print(f"Введенный список - {start_list}")
print(f"Измененный список - {change_list}")
