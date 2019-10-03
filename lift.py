class Lift():

    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.floors = []

    def next_floor(self):
        return self.floors.pop(0)

    def requested_floor(self, floor):
        self.floors.append(floor)
