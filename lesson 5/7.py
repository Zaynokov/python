import json
with open("firms(7).txt", "r", encoding="utf-8") as f:
    data = f.read().splitlines()

forms = ["ИП", "ООО"]


def cash(firm):
    firm = firm.split()
    return int(firm[-2]) - int(firm[-1])


def firm_name(firm):
    names = ""
    for i in firm.split():
        if i in forms:
            break
        names += i + " "
    return names[0:-1]


s = 0
k = 0
for i in range(len(data)):
    if cash(data[i]) > 0:
        s += cash(data[i])
        k += 1

result = [{}, {"average_profit": s / k}, {}]

for i in range(len(data)):
    if cash(data[i]) > 0:
        result[0].update({firm_name(data[i]): cash(data[i])})
    else:
        result[2].update({firm_name(data[i]): cash(data[i])})

with open("result(7).json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False)
