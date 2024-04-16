import machine # type: ignore
import utime # type: ignore
import env
import esp8266_utils

is_led_on = False
is_always_on = False

led_green = machine.Pin(4, machine.Pin.OUT)
led_strip = machine.Pin(7, machine.Pin.OUT)
always_on_button = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)

def always_on_button_handler(pin):
  global is_led_on
  global is_always_on

  if is_always_on:
    is_led_on = False
    led_green.value(0)
    led_strip.value(0)
  else:
    is_led_on = True
    led_green.value(1)
    led_strip.value(1)

  is_always_on = not is_always_on

  print('is_always_on', is_always_on)
  print('is_led_on', is_led_on)

def handle_led_strip(hour):
  if is_always_on:
    return True

  global is_led_on

  if hour >= env.LED_ON_HOUR and hour <= env.LED_OFF_HOUR:
    if not is_led_on:
      is_led_on = True
      led_strip.value(1)
  else:
    if is_led_on:
      is_led_on = False
      led_strip.value(0)

  print('is_led_on', is_led_on)

def run():
  utc_offset = 7 * 60 * 60

  # Pin is always in high (3.3V) by default => need to trigger with GND pin.
  always_on_button.irq(trigger=machine.Pin.IRQ_FALLING, handler=always_on_button_handler)

  while True:
    now = utime.localtime(utime.time() + utc_offset)
    hour = now[3]
    handle_led_strip(hour)

    # Sync. time periodically to keep RTC works exactly.
    if hour % 23 == 0:
      esp8266_utils.sync_ntp_time()

    utime.sleep(15)
