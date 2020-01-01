from microbit import *
import neopixel
from random import randint


def turnOddTheLights():
    np[0] = (0, 0, 0)
    np.show()

np = neopixel.NeoPixel(pin1, 1)
turnOddTheLights()
while True:
    if button_a.was_pressed():
        for pixel_id in range(0, 10):
            red = randint(0, 60)
            green = randint(0, 60)
            blue = randint(0, 60)
            np[0] = (red, green, blue)
            np.show()
            sleep(1000)
        turnOddTheLights()
    if button_b.was_pressed():
        turnOddTheLights()


