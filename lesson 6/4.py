class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        self.direction = direction
        print(f"Машина повернула на{self.direction}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Превышена допустимая скорость движения")
        else:
            print(f"Скорость автомобиля {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Превышена допустимая скорость движения")
        else:
            print(f"Скорость автомобиля {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


town_car = TownCar(55, "red", "Lincoln", False)
sport_car = SportCar(120, "blue", "Lamborghini", False)
work_car = WorkCar(41, "green", "Tractor", False)
police_car = PoliceCar(80, "white", "Alpha Romeo", True)

print(town_car.speed)
print(sport_car.color)
print(work_car.name)
print(sport_car.is_police)
print(police_car.is_police)

town_car.show_speed()
sport_car.turn("лево")
work_car.go()
police_car.stop()
