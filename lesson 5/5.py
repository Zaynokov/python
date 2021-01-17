from random import randint
with open("random_numbers(5).txt", "w+") as file:
    for i in range(randint(10, 21)):
        file.write(f"{randint(0, 25)} ")
    file.seek(0)
    numbers = file.read()

print(f"Сумма всех чисел равна: {sum(map(int, numbers.split()))}")
