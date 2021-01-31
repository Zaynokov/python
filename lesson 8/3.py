class DigitalList(Exception):
    def __init__(self, txt):
        self.txt = txt


result = []
run = True
while run:
    try:
        n = input("Введите элемент\nДля выхода введите 'q': ")
        if n.isdigit():
            result.append(int(n))
        elif n.lower() == 'q':
            run = False
        else:
            raise DigitalList("Вы ввели не число. Продолжайте ввод")
    except DigitalList as error:
        print(error)
print("-"*20)
print(result)
