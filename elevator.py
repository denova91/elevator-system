class coordinator:
    floors = []

    def __init__(self, count_elevator):
        self.count_elevator = count_elevator

    def call(self, num_floors):
        if self.floors.count(num_floors):
            if self.floors == num_floors:
                return elevator.open()
            else:
                return elevator.movement(num_floors)
        else:
            print(f'Error: в доме нет этажа {num_floors}')

class elevator:

    def __init__(self, max_weight, speed, doors, floor):
        self.max_weight = max_weight
        self.speed = speed
        self.doors = doors
        self.floor = floor

    def movement(self, n):
        if isinstance(n, int):
            if self.floors.count(n):
                self.floor = n
            else:
                print(f'Error: в доме нет этажа {n}')
        else:
            print("Error: этаж должно быть числом")

    def open(self):
        self.doors = True
        print("Двери открыты")

    def close(self):
        self.doors = False
        print("Двери закрыты")
    