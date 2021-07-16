class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self._income = is_police

    def go(self):
        print(f"{self.name} поехал(-а)!")

    def stop(self):
        print(f"{self.name} остановился(-лась).")

    def turn(self, direction):
        self.direction = direction
        if self.direction.lower() == "right" or self.direction.lower() == "направо":
            print("Машина повернула направо")

        if self.direction.lower() == "left" or self.direction.lower() == "налево":
            print("Машина повернула налево")

        if self.direction.lower() == "forward" or self.direction.lower() == "вперёд":
            print("Машина поехала вперёд")

        if self.direction.lower() == "back" or self.direction.lower() == "назад":
            print("Машина развернулась назад")

    def show_speed(self):
        print(f'{self.name} едит со скоростью {self.speed}км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} едит со скоростью {self.speed}км/ч. Скорось привышена!!!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} едит со скоростью {self.speed}км/ч. Скорось привышена!!!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town = TownCar(120, "black", "KIA")
sport = SportCar(240, "blue", "Bugatti")
work = WorkCar(60, "white", "KAMAZ")
police = PoliceCar(160, "white-blue", "Chevrolet-police")

town.go()
town.show_speed()
town.stop()

sport.go()
sport.show_speed()
sport.stop()

work.go()
work.show_speed()
work.stop()

police.go()
police.show_speed()
police.stop()