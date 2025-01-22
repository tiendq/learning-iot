import machine # type: ignore
import neopixel # type: ignore
import utime # type: ignore
import env
import esp8266_utils
import light_effect

# Note that on method of a Pin might turn the LED off and off might turn it on (or vice versa),
# depending on how the LED is wired on your board.
led_onboard = machine.Pin(2, machine.Pin.OUT)
led_strip = machine.Pin(5, machine.Pin.OUT)
neo_pixels = neopixel.NeoPixel(led_strip, 25)
# always_on_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

# is_led_on = False
# is_always_on = False

def always_on_button_handler(pin):
  global is_led_on
  global is_always_on

  print('button pressed')

  if is_always_on:
    is_led_on = False
    led_onboard.value(1) # off
    light_effect.clear_pixels(pixels)
  else:
    is_led_on = True
    led_onboard.value(0) # on
    light_effect.turn_on_white(pixels)

  is_always_on = not is_always_on

  print('is_always_on', is_always_on)
  print('is_led_on', is_led_on)

def handle_led_strip(hour, pixels):
  # if is_always_on:
  #  return True

  # global is_led_on

  if hour >= env.LED_ON_HOUR and hour < env.LED_OFF_HOUR:
  #  if not is_led_on:
  #    is_led_on = True
      light_effect.turn_sunlight_on(pixels)
  else:
  #  if is_led_on:
  #    is_led_on = False
      light_effect.turn_sunlight_off(pixels)

  # print('is_led_on', is_led_on)

def run():
  utc_offset = 7 * 60 * 60

  # It's worth doing a reset since colors might be not displayed correctly.
  light_effect.clear_pixels(neo_pixels)
  # always_on_button.irq(trigger=machine.Pin.IRQ_FALLING, handler=always_on_button_handler)

  while True:
    now = utime.localtime(utime.time() + utc_offset)
    hour = now[3]
    handle_led_strip(hour, neo_pixels)

    # Synchronize time every day to keep RTC works exactly.
    if hour % 21 == 0:
      esp8266_utils.sync_ntp_time()

    utime.sleep(15)
