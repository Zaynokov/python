rating = [12, 9, 9, 8, 5, 3, 3]
while True:
    new_element_count = input("Сколько новых элементов хотите добавить?\n Введите целое положительное число - ")
    if new_element_count.isdigit():
        new_element_count = int(new_element_count)
        break
for i in range(new_element_count):
    while True:
        new_element = input("Введите новый элемент рейтинга (Целое положительное число) - ")
        if new_element.isdigit():
            new_element = int(new_element)
            rating.append(new_element)
            break
rating.sort(reverse=True)
print(rating)
