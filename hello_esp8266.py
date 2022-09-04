import machine
import network
import utime

# Note that on method of a Pin might turn the LED off and off might turn it on (or vice versa),
# depending on how the LED is wired on your board.
led_onboard = machine.Pin(2, machine.Pin.OUT)
led_onboard.off()
utime.sleep(1)
led_onboard.on() # it actually turned off :O

sta_if = network.WLAN(network.STA_IF)
sta_if.active()

ap_if = network.WLAN(network.AP_IF)
ap_if.active()
print(ap_if.ifconfig())
ap_if.active(False)
