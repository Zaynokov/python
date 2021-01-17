with open("eng_num(4).txt", "r", encoding="utf-8") as file:
    data = file.read().splitlines()
res = []
d = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
for i, k in enumerate(data):
    res.append(k.replace(list(d)[i], d[list(d)[i]]))

with open("rus_num(4).txt", "w", encoding="utf-8") as f:
    for i in res:
        f.writelines(i + "\n")
