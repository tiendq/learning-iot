import machine
import neopixel
import utime

GPIO_PIN = 5
LED_COUNT = 20

pixels = neopixel.NeoPixel(machine.Pin(GPIO_PIN), LED_COUNT)

is_led_on = False
turn_on_hour = 17
turn_off_hour = 21

def handle_led_strip(hour):
  if hour < turn_on_hour:
    return None

  global is_led_on

  if is_led_on:
    if hour >= turn_off_hour:
      is_led_on = False
      for i in range(LED_COUNT):
        pixels[i] = (0, 0, 0)
      pixels.write()
      print('LED off')
  else:
    is_led_on = True
    for i in range(LED_COUNT):
      pixels[i] = (225, 225, 225)
    pixels.write()
    print('LED on')

# Note that on method of a Pin might turn the LED off and off might turn it on (or vice versa),
# depending on how the LED is wired on your board.
led_onboard = machine.Pin(2, machine.Pin.OUT)

def start():
  led_onboard.off()
  utime.sleep_ms(500)
  led_onboard.on()  # it actually turns the LED off!

  for i in range(LED_COUNT):
    pixels[i] = (0, 0, 0)
  pixels.write()

  utc_offset = 7 * 60 * 60
  while True:
    now = utime.localtime(utime.time() + utc_offset)
    handle_led_strip(now[3])
    utime.sleep(60)
