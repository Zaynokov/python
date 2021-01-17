with open("data(6).txt", "r", encoding="utf-8") as f:
    data = f.read().splitlines()

result = {}


def name_c(text):
    txt = ""
    c = ''.join([k for k in text if k.isdigit() or k == " "]).split()
    c = sum(list(map(int, c)))
    for k in text:
        if k == ":":
            break
        txt += k
    return txt, c


for i, item in enumerate(data):
    result.update({name_c(data[i])[0]: name_c(data[i])[1]})

print(result)
