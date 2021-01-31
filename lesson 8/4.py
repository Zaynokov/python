from abc import abstractmethod


class Warehouse:
    pass


class OfficeEquip:
    def __init__(self, name, color, price, service_life, paper_size, speed):
        self.color = color
        self.name = name
        self.price = price
        self.service_life = service_life
        self.paper_size = paper_size
        self.speed = speed


class MFU(OfficeEquip):
    def __init__(self, name, color, price, service_life, paper_size, speed, scan_type, max_resolution):
        OfficeEquip.__init__(self, name, color, price, service_life, paper_size, speed)
        self.scan_type = scan_type
        self.max_resolution = max_resolution

    @abstractmethod
    def scan_and_print(self, command):
        if command == 'scan':
            print("Сканирование")
        elif command == 'print':
            print("Печать")
        else:
            print("Неизвестная команда")


class Printer(MFU):
    def __init__(self, name, color, price, service_life, paper_size, speed, max_resolution):
        OfficeEquip.__init__(self, name, color, price, service_life, paper_size, speed)
        self.max_resolution = max_resolution

    def scan_and_print(self, command='print'):
        if command == 'print':
            print("Печать")
        else:
            print("Неизвестная команда")


class Scanner(MFU):
    def __init__(self, name, color, price, service_life, paper_size, speed, scan_type):
        OfficeEquip.__init__(self, name, color, price, service_life, paper_size, speed)
        self.scan_type = scan_type

    def scan_and_print(self, command='scan'):
        if command == 'scan':
            print("Сканирование")
        else:
            print("Неизвестная команда")
