import asyncio
import torch

class Elevator:

    def __init__(self, max_weight: int, doors: bool, floor: int):
        self.max_weight = max_weight
        self.doors = doors
        self.floor = floor

    async def move_to(self, passenger_time: int = 10):
        await asyncio.sleep()
        pass
                

    def open(self):
        self.doors = True
        print("Двери открыты")

    def close(self):
        self.doors = False
        print("Двери закрыты")

class Coordinator:
    
    def __init__(self, need_floors: list[int], parametr_house: list):
        self.need_floors = need_floors
        self.house = torch.zeros(parametr_house)

        print(f"Координатор создан. Лифтов в системе: {len(self.elevators)}")

    def time(self, cnt: int):
        return cnt*6 # скорость лифтов равна 10 этажей в минуту

    def call(self, num_floor: int, target_floor: int):
        self.target_floor = target_floor
        if num_floor in self.max_floors:
            if self.find_nearest(num_floor) == num_floor:
                print("Лифт уже на этом этаже")
                return self.elevator.open()
            else:
                return self.movement(num_floor)
        else:
            print(f'Error: в доме нет этажа {num_floor}')

    def find_nearest(self):
        best_elevator = None
        min_dist = 999
        self.target_floor = self.target_floor
        for elevator in self.elevators:
            dist =  abs(self.target_floor - elevator.floor)
            if dist < min_dist:
                min_dist = dist
                best_elevator = elevator
        return best_elevator
    