revenue = int(input("Введите размер выручки фирмы - "))
expenses = int(input("Введите размер издержек фирмы - "))

if revenue - expenses > 0:
    print(f"Прибыльное дело!\nРентабельность выручки равна {(revenue - expenses) / revenue}")
    personal = int(input("Введите численность сотрудниокв - "))
    print(f"Прибыль фирмы в расчете на одного сотрудника равна {(revenue - expenses) / personal}")
elif revenue == expenses:
    print("Доходы равны расходам")
else:
    print("Фирма терпит убыток")
