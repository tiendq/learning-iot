import machine
import neopixel
import utime
import light_effect

DIN_PIN = 5
#LED_ONBOARD_PIN = 25 # Pico
LED_ONBOARD_PIN = 2 # ESP8266
#LED_COUNT = 10 # Pico
LED_COUNT = 20 # ESP8266

pixels = neopixel.NeoPixel(machine.Pin(DIN_PIN), LED_COUNT)

is_led_on = False
turn_on_hour = 17
turn_off_hour = 21

def clear_pixels(pixels):
  for i in range(len(pixels)):
    pixels[i] = (0, 0, 0)
  pixels.write()

def set_all_white(pixels):
  for i in range(len(pixels)):
    pixels[i] = (225, 225, 225)
  pixels.write()

def run_effects(hour, minute):
  x = minute % 5

  if 0 == x:
    print('running rainbow_cycle')
    for i in range(10):
      light_effect.rainbow_cycle(pixels, 10)

def handle_led_strip(hour, minute):
  if hour < turn_on_hour:
    return None

  global is_led_on

  if is_led_on:
    if hour >= turn_off_hour:
      is_led_on = False
      clear_pixels(pixels)
      print('LED turned off')
    else:
      run_effects(hour, minute)
      utime.sleep_ms(300)
      set_all_white(pixels)

  if not is_led_on and hour < turn_off_hour:
    is_led_on = True
    set_all_white(pixels)
    print('LED turned on')

# Note that on method of a Pin might turn the LED off and off might turn it on (or vice versa),
# depending on how the LED is wired on your board.
led_onboard = machine.Pin(LED_ONBOARD_PIN, machine.Pin.OUT)

def start():
  led_onboard.off()
  utime.sleep_ms(500)
  led_onboard.on()  # it actually turns the LED off!

  # It's worth doing a reset since colors might be not displayed correctly.
  clear_pixels(pixels)

  # utc_offset = 0 # emulation mode
  utc_offset = 7 * 60 * 60 # production mode
  while True:
    now = utime.localtime(utime.time() + utc_offset)
    # print('local time: ', now)
    handle_led_strip(now[3], now[4])
    utime.sleep(60)
