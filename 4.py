number = int(input("Введите целое положительное число - "))

maximum = 0
while number > 0:
    if number % 10 > maximum:
        maximum = number % 10
    number = number // 10

print(f"Наибольшая цифра в введенном числе {maximum}")
