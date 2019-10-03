import random


class Lift:

    def __init__(self, display):
        self.num_floors = display.floors
        self.floors = []
        self.display = display
        self.going_up = 1
        self.floor = 0

    def next_floor(self):
        while 1:
            yield self.floor
            if self.floors:
                self.floor = self.floors.pop(self.closest_floor())
            else:
                self.floor = random.randint(self.num_floors)

    def requested_floor(self, floor):
        self.floors.append(floor)

    def start(self):
        for floor in self.next_floor():
            self.display.send_lift_to(floor)

    def closest_floor(self):
        return sorted(self.floors, key=self.sort_key)[0]

    def sort_key(self, next_floor):
        if next_floor < self.floor and self.going_up:
            next_floor -= self.num_floors
        elif next_floor > self.floor and not self.going_up:
            next_floor += self.num_floors
        return abs(self.floor - next_floor)
