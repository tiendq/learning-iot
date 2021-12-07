# traffic_lights.py

import machine
import utime
import _thread

global button_pressed
button_pressed = False

led_red = machine.Pin(15, machine.Pin.OUT)
led_yellow = machine.Pin(12, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
led_walker = machine.Pin(11, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

# turn on light for pedestrians.
def button_reader_thread():
    global button_pressed
    while True:
        if 1 == button.value():
            button_pressed = True
        utime.sleep(0.1)

led_red.off()
led_yellow.off()
led_green.off()
led_walker.off()

_thread.start_new_thread(button_reader_thread, ())

while True:
    led_red.on()
    utime.sleep(5)
    if True == button_pressed:
        led_walker.on()
        utime.sleep(5)
        led_walker.off()
        button_pressed = False
    led_red.off()
    led_green.on()
    utime.sleep(3.5)
    led_green.off()
    led_yellow.on()
    utime.sleep(1.5)
    led_yellow.off()
