# test_effect.py

import machine
import neopixel
import utime
import light_effect

DIN_PIN = 5
LED_ONBOARD_PIN = 25 # Pico
LED_COUNT = 10 # Pico

pixels = neopixel.NeoPixel(machine.Pin(DIN_PIN), LED_COUNT)

for i in range(LED_COUNT):
  pixels[i] = (0, 0, 0)
pixels.write()

light_effect.rainbow_cycle(pixels, 100)
