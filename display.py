import time
import os


class Display:
    def __init__(self, floors, lifts):
        self.floors = floors
        self.lifts = lifts
        self.position = 0

    def send_lift_to(self, floor):
        floors = range(self.position, floor + 1, 1 if floor > self.position else -1)
        for i in floors:
            # print(i)
            self.draw(i)

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
                print(full_floor)
            else:
                print(empty_floor)

        print(ground)
        time.sleep(0.5)


if __name__ == "__main__":
    display = Display(10, 1)
    display.send_lift_to(5)
    # display.send_lift_to(5)

