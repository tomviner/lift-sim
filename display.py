import time
import os

class Display:
    def __init__(self, floors, lifts):
        self.floors = floors
        self.lifts = lifts
        self.position = 0

    def send_lift_to(self, floor):
        step = 1 if floor > self.position else -1
        floors = range(self.position, floor + step, step)
        for i in floors:
            # print(i)
            self.draw(i)
            self.position =i

    def draw(self, floor):
        """
        ___________________
        |                 |
        |                 |
        |                 |
        |                 |
        |                 |
        |                 |
        |                 |
        |                 |
        |                 |
        |                 |
        |                 |
        |   ||            |
        |                 |
        -------------------
        """
        os.system('clear')

        roof = '___________________'
        ground = '___________________'
        empty_floor = '|                 |'
        full_floor = '|   ||            |'

        print(roof)
        for j in range(self.floors, -1, -1):
            if j == floor:
                print(full_floor, j)
            else:
                print(empty_floor, j)

        print(ground)
        time.sleep(0.2)


if __name__ == "__main__":
    display = Display(10, 1)
    display.send_lift_to(7)
    display.send_lift_to(3)

