print("Введите данные построчно\nДля выхода отправьте пустой ввод")
with open("user_input(1).txt", "w") as file:
    while True:
        data = input()
        if data == "":
            break
        else:
            file.write(f"{data}\n")
