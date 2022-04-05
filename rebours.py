


import time
from sense_emu import SenseHat

sense = SenseHat()

R = (255, 0, 0)

for i in reversed(range(0,10)):
    sense.show_letter(str(i), R)
    time.sleep(1)