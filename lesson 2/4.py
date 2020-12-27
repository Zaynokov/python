text = input("Введите несколько слов, разделенных пробелом - ")
n = 1
for i in text.split():
    print(f"{n} - {i[0:10]}")
    n += 1
