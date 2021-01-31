class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def int_date(cls, str_date):
        return list(map(int, str_date.split("-")))

    @staticmethod
    def validation(str_date):
        date = list(map(int, str_date.split("-")))
        if date[1] in [1, 3, 5, 7, 8, 10, 12]:
            if 0 < date[0] <= 31:
                if date[2] > 0:
                    return "Дата введена корректно"
                else:
                    return "Дата введена некорректно"
            else:
                return "Дата введена некорректно"
        elif date[1] in [4, 6, 9, 11]:
            if 0 < date[0] <= 30:
                if date[2] > 0:
                    return "Дата введена корректно"
                else:
                    return "Дата введена некорректно"
            else:
                return "Дата введена некорректно"
        elif date[1] == 2:
            if date[2] > 0 and date[2] % 4 == 0:
                if 0 < date[0] <= 29:
                    return "Дата введена корректно"
                else:
                    return "Дата введена некорректно"
            elif date[2] > 0 and date[2] % 4 != 0:
                if 0 < date[0] <= 28:
                    return "Дата введена корректно"
                else:
                    return "Дата введена некорректно"
            else:
                return "Дата введена некорректно"
        else:
            return "Дата введена некорректно"


print(Date.validation("29-02-2021"))
print(Date.validation("9-5-2021"))
d = Date
print(d.int_date("12-3-13"))
