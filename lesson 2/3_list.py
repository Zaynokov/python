month = input("Введите месяц (число от 1 до 12) - ")
season_list = [["Зима", 1, 2, 12], ["Весна", 3, 4, 5], ["Лето", 6, 7, 8], ["Осень", 9, 10, 11]]

while True:
    if month.isdigit() and (int(month) >= 1) and (int(month) <= 12):
        for i in season_list:
            if int(month) in i:
                print(f"Время года - {i[0]}")
        break
    else:
        month = input("Пожалуйста, введите число от 1 до 12 - ")
