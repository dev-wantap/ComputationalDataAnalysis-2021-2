class Car:
    color: str = ""
    speed: int = 0
    count = 0

    def __init__(self, icolor: str, ispeed: int):
        self.color = icolor
        self.speed = ispeed
        Car.count += 1

    def up_speed(self, value: int):
        self.speed = value
        print(f"현재 속도(Super Class) : {self.speed}")

    def print_info(self):
        print(f'자동차의 색상은 {self.get_color()}이며, 현재 속도는 {self.get_speed()} km 입니다. (총 {Car.count}대)')

    def get_color(self):
        return self.color

    def get_speed(self):
        return self.speed


class Sedan(Car):
    seat_num = 0

    def __init__(self, icolor: str, ispeed: int):
        super().__init__(icolor, ispeed)
        self.seat_num = 0

    def get_seat_num(self):
        return self.seat_num

    def print_info_sedan(self):
        print(f'자동차의 색상은 {self.get_color()}이며, 현재 속도는 {self.get_speed()} km 입니다. (총 {Car.count}대)\n'
              f'좌석수는 {self.seat_num}개 입니다.')


class Truck(Car):
    capacity = 0

    def up_speed(self, value: int):
        self.speed = value

        if self.speed > 110:
            self.speed = 110

        print(f"현재 속도 (SubClass) : {self.speed}")

    def get_capacity(self):
        return self.capacity

    def print_info_sedan(self):
        print(f'자동차의 색상은 {self.get_color()}이며, 현재 속도는 {self.get_speed()} km 입니다. (총 {Car.count}대)\n'
              f'중략은 {self.capacity} 입니다.')


sonata = Sedan('Black', 200)
truck = Truck('Gray', 80)
sonata.up_speed(300)
truck.up_speed(150)
