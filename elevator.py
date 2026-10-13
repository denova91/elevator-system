from time import sleep

class Elevator:

    def __init__(self, max_weight, doors, floor):
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
    
    def __init__(self, count_elevator, elevator_obj, max_floors):
        self.count_elevator = count_elevator
        self.elevator = elevator_obj
        self.max_floors = max_floors

    def time(self, cnt):
        return cnt*6 # скорость лифтов равна 10 этажей в минуту

    def call(self, num_floor):
        if num_floor in self.max_floors:
            if self.elevator.floor == num_floor:
                print("Лифт уже на этом этаже")
                return self.elevator.open()
            else:
                return self.movement(num_floor)
        else:
            print(f'Error: в доме нет этажа {num_floor}')

    def movement(self, target_floor, passenger_time=10):
        if target_floor in self.max_floors:
            self.elevator.close()
            sleep(self.time(abs(target_floor - self.elevator.floor)))
            self.elevator.floor = target_floor
            print(f"Лифт переместился на {target_floor} этаж")
            self.elevator.open()
            sleep(passenger_time)
            self.elevator.close()