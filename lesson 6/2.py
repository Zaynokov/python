road_l = int(input("Введите длину дороги в метрах - "))
road_w = int(input("Введите ширину дороги в метрах - "))


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        return f"{self._width * self._length * 125 // 1000} т"


road_weight = Road(road_l, road_w)
print(road_weight.weight())
