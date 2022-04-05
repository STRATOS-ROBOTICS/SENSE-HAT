import time
from sense_emu import SenseHat

sense = SenseHat()


sense.clear(255, 255, 255)
sense.low_light = True
time.sleep(2)
sense.low_light = False