month = input("Введите месяц (число от 1 до 12) - ")
season_dict = {"Зима": ["12", "1", "2"],
               "Весна": ["3", "4", "5"],
               "Лето": ["6", "7", "8"],
               "Осень": ["9", "10", "11"]}
while True:
    if month.isdigit() and (int(month) >= 1) and (int(month) <= 12):
        for i in list(season_dict.keys()):
            if month in season_dict.get(f"{i}"):
                print(i)
        break
    else:
        month = input("Пожалуйста, введите число от 1 до 12 - ")
