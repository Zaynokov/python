items_list = []
list_of_dict = []
an_dict = {}
name = []
price = []
pieces = []
while True:
    n = input("Сколько видов товаров добавить? - ")
    if n.isdigit():
        n = int(n)
        break
for i in range(n):
    list_of_dict.append({})
    list_of_dict[i]["Название товара"] = input(f"Введите название {i + 1}-го товара - ")
    name.append(list_of_dict[i]["Название товара"])
    list_of_dict[i]["Цена товара"] = \
        input(f"Введите цену {i + 1}-го товара ({list_of_dict[i].get('Название товара')}) - ")
    price.append(list_of_dict[i]["Цена товара"])
    list_of_dict[i]["Количество товара"] = \
        input(f"Введите количество {i + 1}-го товара ({list_of_dict[i].get('Название товара')}) - ")
    pieces.append(list_of_dict[i]["Количество товара"])
    list_of_dict[i]["Единица изм-я"] = \
        input(f"Введите единицу измерения {i + 1}-го товара ({list_of_dict[i].get('Название товара')}) - ")
    items_tuple = (i + 1, list_of_dict[i])
    items_list.append(items_tuple)
    an_dict["Название товара"] = name
    an_dict["Цена товара"] = price
    an_dict["Количество товара"] = pieces
print(*items_list, sep="\n")
an_dict["Единица изм-я"] = "шт"
print(an_dict)
