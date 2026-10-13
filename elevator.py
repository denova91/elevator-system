from time import sleep

class Elevator:

    def __init__(self, max_weight: int, doors: bool, floor: int):
        self.max_weight = max_weight
        self.doors = doors
        self.floor = floor


    def open(self):
        self.doors = True
        print("Двери открыты")

    def close(self):
        self.doors = False
        print("Двери закрыты")

class Coordinator:
    
    def __init__(self, count_elevator: int, elevator_obj: int, max_floors: list[int]):
        self.count_elevator = count_elevator
        self.elevator = elevator_obj
        self.max_floors = max_floors

    def time(self, cnt: int):
        return cnt*6 # скорость лифтов равна 10 этажей в минуту

    def call(self, num_floor: int):
        if num_floor in self.max_floors:
            if self.elevator.floor == num_floor:
                print("Лифт уже на этом этаже")
                return self.elevator.open()
            else:
                return self.movement(num_floor)
        else:
            print(f'Error: в доме нет этажа {num_floor}')

    def movement(self, target_floor: int, passenger_time: int = 10):
        if target_floor in self.max_floors:
            self.elevator.close()
            sleep(self.time(abs(target_floor - self.elevator.floor)))
            self.elevator.floor = target_floor
            print(f"Лифт переместился на {target_floor} этаж")
            self.elevator.open()
            sleep(passenger_time)
            self.elevator.close()