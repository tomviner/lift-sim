import sys

from display import Display
from lift import Lift

display = Display(int(sys.argv[1]), 0)

lift = Lift(display)

lift.start()
