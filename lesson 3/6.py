while True:
    text = input("Введите слово из маленьких латинских букв: ")
    helper = text.replace(" ", "")
    if helper.isalpha() and ord("a") <= ord(min(list(helper), key=ord)) <= ord("z"):
        break

text_list = text.split()
result = []


def int_func(txt):
    return txt[0].upper() + txt[1::]


for i in text_list:
    result.append(int_func(i))

print(" ".join(result))
