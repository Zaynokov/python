from time import sleep

user_color = input("Какой цвет горел, когда Вы подъехали к светофору?\nВведите цвет на английском - ").lower()


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == "red":
            print(f"\033[31m{self.__color}")
        elif self.__color == "green":
            print(f"\033[32m{self.__color}")
        elif self.__color == "yellow":
            print(f"\033[33m{self.__color}")
        else:
            print("Такого цвета нет в светофоре :-(\nПерезапустите программу")
        for i in range(10):
            if self.__color == "red":
                self.__color = "yellow"
                for r in range(7):
                    print(7 - r, end=" " if 7 - r > 1 else "\n")
                    sleep(1)
                print(f"\033[33m{self.__color}")
            elif self.__color == "yellow":
                self.__color = "green"
                for r in range(2):
                    print(2 - r, end=" " if 2 - r > 1 else "\n")
                    sleep(1)
                print(f"\033[32m{self.__color}")
            elif self.__color == "green":
                self.__color = "red"
                for r in range(10):
                    print(10 - r, end=" " if 10 - r > 1 else "\n")
                    sleep(1)
                print(f"\033[31m{self.__color}")


tl = TrafficLight(user_color)
tl.running()
