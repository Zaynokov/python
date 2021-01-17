with open("salary(3).txt", "r", encoding="utf-8") as file:
    data = file.read().splitlines()
total = 0


def div(text):
    surname = ''.join([j for j in text if not j.isdigit()])
    salary = ''.join([k for k in text if k.isdigit()])
    return surname[0:-1], int(salary)


print("Список сотрудников, имеющих оклад меньше 20 тыс.")

for i in data:
    total += div(i)[1]
    if div(i)[1] < 20000:
        print(div(i)[0])
print(f"Средний оклад сотрудников: {total // len(data)}")
