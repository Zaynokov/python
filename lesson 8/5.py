from abc import abstractmethod


class Warehouse:

    def __init__(self):
        self.storage = {}

    def add_equip(self, device, info):
        if device.upper() == 'MFU':
            self.storage.update({'MFU': info})
        elif device.lower() == 'printer':
            self.storage.update({'printer': info})
        elif device.lower() == 'scanner':
            self.storage.update({'scanner': info})
        return self.storage

    def take(self, section, device, quantity):
        result_1 = self.storage[device].copy()
        result_1.update({"Количество": quantity})
        result_2 = {"Отдел": section, "Устройство": device}
        result_2.update({"Информация": result_1})
        self.storage[device].update({"Количество": self.storage[device]["Количество"] - quantity})
        return result_2

    def __str__(self):
        res = ''
        for k, eq in self.storage.items():
            res += f"{str(k)}: "
            res += f"{str(eq)}\n"
        return res


class OfficeEquip:
    def __init__(self, name, quantity, color, price, service_life, paper_size, speed):
        self.color = color
        self.name = name
        self.quantity = quantity
        self.price = price
        self.service_life = service_life
        self.paper_size = paper_size
        self.speed = speed


class MFU(OfficeEquip):
    def __init__(self, name, quantity, color, price, service_life, paper_size, speed, scan_type, max_resolution):
        OfficeEquip.__init__(self, name, quantity, color, price, service_life, paper_size, speed)
        self.scan_type = scan_type
        self.max_resolution = max_resolution

    @abstractmethod
    def scan_and_print(self, command):
        if command.lower() == 'scan':
            print("Сканирование...")
        elif command.lower() == 'print':
            print("Печать...")
        else:
            print("Неизвестная команда")

    def info(self):
        info = {
                "Название": self.name,
                "Количество": self.quantity,
                "Цвет": self.color,
                "Цена": self.price,
                "Срок службы": self.service_life,
                "Формат бумаги": self.paper_size,
                "Скорость работы": self.speed,
                "Тип сканера": self.scan_type,
                "Максимальное разрешение": self.max_resolution
                }
        return info


class Printer(MFU):
    def __init__(self, name, quantity, color, price, service_life, paper_size, speed, max_resolution):
        OfficeEquip.__init__(self, name, quantity, color, price, service_life, paper_size, speed)
        self.max_resolution = max_resolution

    def scan_and_print(self, command='print'):
        if command.lower() == 'print':
            print("Печать...")
        else:
            print("Неизвестная команда")

    def info(self):
        return {
                "Название": self.name,
                "Количество": self.quantity,
                "Цвет": self.color,
                "Цена": self.price,
                "Срок службы": self.service_life,
                "Формат бумаги": self.paper_size,
                "Скорость работы": self.speed,
                "Максимальное разрешение": self.max_resolution
                }


class Scanner(MFU):
    def __init__(self, name, quantity, color, price, service_life, paper_size, speed, scan_type):
        OfficeEquip.__init__(self, name, quantity, color, price, service_life, paper_size, speed)
        self.scan_type = scan_type

    def scan_and_print(self, command='scan'):
        if command.lower() == 'scan':
            print("Сканирование...")
        else:
            print("Неизвестная команда")

    def info(self):
        return {
                "Название": self.name,
                "Количество": self.quantity,
                "Цвет": self.color,
                "Цена": self.price,
                "Срок службы": self.service_life,
                "Формат бумаги": self.paper_size,
                "Скорость работы": self.speed,
                "Тип сканера": self.scan_type
                }


warehouse = Warehouse()
mfu = MFU("Xerox B205", 30, "white", 30000, 15, "A4", (30, "стр/мин"), "ADF", (1200, 1200))
printer = Printer("Phaser 3052", 20, "white", 25000, 13, "A4", (26, "стр/мин"), (4800, 600))
scanner = Scanner("Duplex", 25, "white", 24000, 14, "A4", (1000, "стр/день"), "Портативный")

warehouse.add_equip("scanner", scanner.info())
warehouse.add_equip("printer", printer.info())
warehouse.add_equip("MFU", mfu.info())

print(warehouse)
print("-" * (len(str(warehouse)) // 3))
print(warehouse.take("Бухгалтерия", "printer", 2))
print(warehouse.take("Контент", "scanner", 1))
print("-" * (len(str(warehouse)) // 3))
print(warehouse)
