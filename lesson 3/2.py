print("Пожалуйста, вводите все данные корректно")
while True:
    name = input("Введите имя: ")
    if name.isalpha():
        break
while True:
    surname = input("Введите фамилию: ")
    if surname.isalpha():
        break
while True:
    birth_year = input("Введите год рождения: ")
    if birth_year.isdigit():
        break
while True:
    city = input("Введите город проживания: ")
    if city.isalpha():
        break
while True:
    email = input("Введите email: ")
    if "@" and "." in email:
        break
while True:
    phone_number = input("Введите номер телефона: ")
    if phone_number.isdigit():
        break


def info(nm, snm, b_year, ct, eml, ph_num):
    return f"Имя - {nm}, Фамилия - {snm}, Год рождения - {b_year}, Город проживания - {ct}, email - {eml}, Номер " \
           f"телефона - {ph_num} "


print(info(nm=name, snm=surname, b_year=birth_year, ct=city, eml=email, ph_num=phone_number))
