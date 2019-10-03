import random


class Lift():

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
                self.floor = self.floors.pop(0)
            else:
                self.floor = random.randint(self.num_floors)

    def requested_floor(self, floor):
        self.floors.append(floor)

    def start(self):
        for floor in self.next_floor():
            self.display.send_lift_to(floor)

    def closest_floor:
        pass
