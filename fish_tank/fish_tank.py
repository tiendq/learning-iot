import machine
import neopixel
import utime

DIN_PIN = 5
# LED_ONBOARD_PIN = 25 # Pico
LED_ONBOARD_PIN = 2 # ESP8266
# LED_COUNT = 10 # Pico
LED_COUNT = 20 # ESP8266

pixels = neopixel.NeoPixel(machine.Pin(DIN_PIN), LED_COUNT)

is_led_on = False
turn_on_hour = 17
turn_off_hour = 21

def handle_led_strip(hour):
  if hour < turn_on_hour:
    return None

  global is_led_on

  if is_led_on and hour >= turn_off_hour:
    is_led_on = False
    for i in range(LED_COUNT):
      pixels[i] = (0, 0, 0)
    pixels.write()
    print('LED turned off')

  if not is_led_on and hour < turn_off_hour:
    is_led_on = True
    for i in range(LED_COUNT):
      pixels[i] = (225, 225, 225)
    pixels.write()
    print('LED turned on')

# Note that on method of a Pin might turn the LED off and off might turn it on (or vice versa),
# depending on how the LED is wired on your board.
led_onboard = machine.Pin(LED_ONBOARD_PIN, machine.Pin.OUT)

def start():
  led_onboard.off()
  utime.sleep_ms(500)
  led_onboard.on()  # it actually turns the LED off!

  # It's worth doing a reset since colors might be not displayed correctly.
  for i in range(LED_COUNT):
    pixels[i] = (0, 0, 0)
  pixels.write()

  # utc_offset = 0 # emulation mode
  utc_offset = 7 * 60 * 60 # production mode
  while True:
    now = utime.localtime(utime.time() + utc_offset)
    handle_led_strip(now[3])
    utime.sleep(60)
